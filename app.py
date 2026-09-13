from flask import Flask, request, jsonify, send_from_directory, Response, make_response
import urllib.request
from flask_cors import CORS
from database import init_db, seed_demo_data, get_db
from astra_engine import process_message
from astra_full import process_full, synthesize_notes, flashcards, learning_path, _clean_reply_text
from werkzeug.security import generate_password_hash, check_password_hash
import os
import uuid
import json
import io
import time
import jwt
from functools import wraps

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app, resources={r"/*": {"origins": "*"}}, allow_headers=["Content-Type", "Authorization", "X-Requested-With", "Accept"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "Sastra AI Capacity Connect",
        "version": "2.0",
        "timestamp": time.time()
    })


JWT_SECRET = 'capacity-connect-dev-secret-change-in-production'
try:
    from config import JWT_SECRET as _JWT_SECRET, JWT_EXPIRY_HOURS
    JWT_SECRET = _JWT_SECRET
except ImportError:
    JWT_EXPIRY_HOURS = 24


def generate_token(user_data):
    """Generate a JWT token for authenticated user."""
    payload = {
        'user_id': user_data['id'],
        'username': user_data['username'],
        'role': user_data['role'],
        'exp': time.time() + (JWT_EXPIRY_HOURS * 3600)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')


def decode_token(token):
    """Decode and validate a JWT token."""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        if payload['exp'] < time.time():
            return None
        return payload
    except (jwt.InvalidTokenError, KeyError):
        return None


def require_auth(f):
    """Decorator requiring valid JWT token."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        if not token:
            # Allow unauthenticated access for demo purposes
            request.current_user = None
            return f(*args, **kwargs)
        payload = decode_token(token)
        if payload:
            request.current_user = payload
        else:
            request.current_user = None
        return f(*args, **kwargs)
    return decorated


def require_role(role):
    """Decorator requiring specific user role."""
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get('Authorization', '').replace('Bearer ', '')
            if not token:
                return jsonify({'error': 'Authentication required'}), 401
            payload = decode_token(token)
            if not payload:
                return jsonify({'error': 'Invalid or expired token'}), 401
            if payload.get('role') != role and payload.get('role') != 'admin':
                return jsonify({'error': 'Insufficient permissions'}), 403
            request.current_user = payload
            return f(*args, **kwargs)
        return decorated
    return decorator


@app.route("/")
def index():
    for candidate in [
        os.path.join(os.path.dirname(__file__), "dist"),
        os.path.join(os.path.dirname(__file__), "frontend", "dist"),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "dist"))
    ]:
        if os.path.exists(os.path.join(candidate, "index.html")):
            return send_from_directory(candidate, "index.html")
    return send_from_directory("templates", "demo.html")


@app.route("/assets/<path:filename>")
def serve_assets(filename):
    for candidate in [
        os.path.join(os.path.dirname(__file__), "dist", "assets"),
        os.path.join(os.path.dirname(__file__), "frontend", "dist", "assets"),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "dist", "assets"))
    ]:
        if os.path.exists(os.path.join(candidate, filename)):
            return send_from_directory(candidate, filename)
    return "", 404


@app.route("/favicon.svg")
def serve_favicon():
    for candidate in [
        os.path.join(os.path.dirname(__file__), "dist"),
        os.path.join(os.path.dirname(__file__), "frontend", "dist"),
        os.path.join(os.path.dirname(__file__), "frontend", "public"),
    ]:
        if os.path.exists(os.path.join(candidate, "favicon.svg")):
            return send_from_directory(candidate, "favicon.svg")
    return "", 404


@app.route("/icons.svg")
def serve_icons():
    for candidate in [
        os.path.join(os.path.dirname(__file__), "dist"),
        os.path.join(os.path.dirname(__file__), "frontend", "dist"),
        os.path.join(os.path.dirname(__file__), "frontend", "public"),
    ]:
        if os.path.exists(os.path.join(candidate, "icons.svg")):
            return send_from_directory(candidate, "icons.svg")
    return "", 404


@app.route("/demo")
def demo_page():
    return send_from_directory("templates", "demo.html")


@app.route("/static/pdfs/<path:filename>")
def serve_pdf(filename):
    pdf_dir = os.path.join(os.path.dirname(__file__), "static", "pdfs")
    response = send_from_directory(pdf_dir, filename, mimetype="application/pdf")
    response.headers["Content-Disposition"] = f'inline; filename="{filename}"'
    response.headers["Cache-Control"] = "public, max-age=3600"
    return response


@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json or {}
    message = data.get("message", "").strip()
    image_data = data.get("image") or data.get("image_data")
    file_data = data.get("file") or data.get("document") or data.get("file_data")
    filename = data.get("filename") or "document.pdf"
    user_id = data.get("user_id")
    user_name = (data.get("user_name") or data.get("username") or "").strip()
    session_id = data.get("session_id", str(uuid.uuid4()))
    explicit_mode = data.get("mode")
    page_ctx = data.get("context") or {}

    # If user_name is provided, lookup from db or keep dynamic external user_name
    if user_name and (not user_id or int(user_id) <= 0):
        conn_lookup = get_db()
        u = conn_lookup.execute("SELECT id, full_name, username FROM users WHERE full_name LIKE ? OR username LIKE ?", 
                                (f"%{user_name}%", f"%{user_name}%")).fetchone()
        if u:
            user_id = u["id"]
            if not user_name:
                user_name = u["full_name"]
        conn_lookup.close()

    # If user_id is provided, get full_name from db if user_name is empty
    if user_id and str(user_id).isdigit() and int(user_id) > 0 and not user_name:
        conn_lookup = get_db()
        u = conn_lookup.execute("SELECT full_name FROM users WHERE id=?", (int(user_id),)).fetchone()
        if u and u["full_name"]:
            user_name = u["full_name"]
        conn_lookup.close()

    if not message and not image_data and not file_data:
        return jsonify({"error": "Message, image, or document file is required"}), 400

    try:
        result = process_full(
            message, user_id, session_id, explicit_mode, page_ctx, 
            image_data=image_data, user_name=user_name, 
            file_data=file_data, filename=filename
        )
        reply = result["reply"]
        extra = {k: v for k, v in result.items() if k != "reply"}
    except Exception as e:
        print(f"[Chat Route Exception]: {e}")
        import traceback
        traceback.print_exc()
        reply = _clean_reply_text(process_message(message, user_id, user_name=user_name))
        extra = {"mode": "learn", "suggestions": []}

    conn = get_db()
    db_user_id = user_id if (user_id and int(user_id) > 0) else None
    conn.execute("INSERT INTO chat_history (user_id,session_id,role,message) VALUES (?,?,?,?)",
                 (db_user_id, session_id, "user", message or f"[Attached {filename}]"))
    conn.execute("INSERT INTO chat_history (user_id,session_id,role,message,metadata) VALUES (?,?,?,?,?)",
                 (db_user_id, session_id, "assistant", reply, json.dumps(extra)))
    conn.commit()
    conn.close()

    out = {"reply": reply, "session_id": session_id}
    out.update(extra)
    return jsonify(out)


@app.route("/api/analyze/document", methods=["POST"])
def analyze_document_endpoint():
    data = request.json or {}
    file_data = data.get("file") or data.get("document") or data.get("file_data")
    filename = data.get("filename", "document.pdf")
    prompt = data.get("prompt") or data.get("message") or "Analyze and summarize this document"
    user_name = data.get("user_name", "Learner")
    user_id = data.get("user_id")

    if not file_data:
        return jsonify({"error": "File/document data in base64 is required"}), 400

    try:
        from document_analyzer import get_document_analyzer
        analyzer = get_document_analyzer()
        doc_info = analyzer.extract_from_base64(file_data, filename=filename)
        analysis_prompt = analyzer.build_analysis_prompt(doc_info, user_query=prompt, user_name=user_name)

        from astra_full import _llm_respond, _clean_reply_text
        context = {"user": {"full_name": user_name, "role": "trainee"}}
        reply = _llm_respond(analysis_prompt, context, history=None, page_ctx={}, mode="learn")
        if not reply:
            reply = f"✦ Document Analysis Completed ({doc_info.get('type', 'doc').upper()} - {doc_info.get('pages', 1)} pages)\n\n" + doc_info.get("text", "")[:600]

        clean_reply = _clean_reply_text(reply)
        return jsonify({
            "reply": clean_reply,
            "filename": filename,
            "doc_type": doc_info.get("type"),
            "pages": doc_info.get("pages"),
            "char_count": doc_info.get("char_count"),
            "mode": "document_analysis"
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Document analysis error: {str(e)}"}), 500


@app.route("/api/image/generate", methods=["POST"])
def generate_image_endpoint():
    data = request.json or {}
    prompt = data.get("prompt", "").strip()
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    try:
        from image_generator import get_image_generator
        gen = get_image_generator()
        res = gen.generate_image(prompt)
        return jsonify(res)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Image generation error: {str(e)}"}), 500


@app.route("/api/image/edit", methods=["POST"])
def edit_image_endpoint():
    data = request.json or {}
    prompt = data.get("prompt", "").strip()
    image_data = data.get("image", "")
    if not prompt or not image_data:
        return jsonify({"error": "Prompt and image are required"}), 400
    
    try:
        from image_generator import get_image_generator
        gen = get_image_generator()
        res = gen.edit_image(image_data, prompt)
        return jsonify(res)
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Image editing error: {str(e)}"}), 500


@app.route("/api/image/proxy", methods=["GET"])
def proxy_image_endpoint():
    url = request.args.get("url", "").strip()
    if not url:
        return jsonify({"error": "URL is required"}), 400
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"
            }
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            content_type = resp.headers.get("Content-Type", "image/jpeg")
            data = resp.read()
            response = make_response(data)
            response.headers["Content-Type"] = content_type
            response.headers["Cache-Control"] = "public, max-age=86400"
            response.headers["Access-Control-Allow-Origin"] = "*"
            return response
    except Exception as e:
        print(f"[ImageProxy] Error fetching remote image: {e}")
        return jsonify({"error": f"Failed to fetch image: {str(e)}"}), 502


@app.route("/api/pdf/generate", methods=["POST"])
def generate_pdf_endpoint():
    data = request.json or {}
    text = data.get("text") or data.get("content") or ""
    title = data.get("title", "Sastra Learning Study Guide")
    topic = data.get("topic", "Digital Capacity Building")
    author = data.get("author", "Sastra AI")

    if not text:
        return jsonify({"error": "Text/content is required for PDF generation"}), 400

    from pdf_generator import get_pdf_generator
    pdf_gen = get_pdf_generator()
    result = pdf_gen.generate_pdf_from_text(text=text, title=title, topic=topic, author=author)
    return jsonify(result)


@app.route("/static/pdfs/<path:filename>", methods=["GET"])
def serve_generated_pdf(filename):
    from pdf_generator import PDF_DIR
    if os.path.exists(os.path.join("/tmp/pdfs", filename)):
        return send_from_directory("/tmp/pdfs", filename)
    if os.path.exists(os.path.join(PDF_DIR, filename)):
        return send_from_directory(PDF_DIR, filename)
    static_fallback = os.path.join(os.path.dirname(__file__), "static", "pdfs")
    return send_from_directory(static_fallback, filename)


@app.route("/api/train/dataset/export", methods=["GET"])
def export_training_dataset():
    from train_dataset_generator import export_all_datasets
    res = export_all_datasets()
    return jsonify({
        "status": "success",
        "datasets": {
            "llama_factory_sft": "/data/astra_llamafactory_sft.json",
            "sharegpt_conversations": "/data/astra_sharegpt_train.json",
            "swe_bench_eval": "/data/swe_bench_agent_eval.json"
        },
        "details": res
    })


@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username", "").strip()
    password = data.get("password", "")

    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
    conn.close()

    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    if user["status"] != "approved":
        return jsonify({"error": f"Account is {user['status']}. Please wait for admin approval."}), 403

    token = generate_token(dict(user))
    return jsonify({
        "id": user["id"],
        "username": user["username"],
        "full_name": user["full_name"],
        "role": user["role"],
        "department": user["department"],
        "token": token
    })


@app.route("/api/auth/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "")
    full_name = data.get("full_name", "").strip()
    role = data.get("role", "trainee")
    department = data.get("department", "")

    if not all([username, email, password, full_name]):
        return jsonify({"error": "All fields are required"}), 400

    if role not in ("trainee", "trainer"):
        return jsonify({"error": "Invalid role"}), 400

    conn = get_db()
    try:
        conn.execute(
            "INSERT INTO users (username,email,password_hash,full_name,role,status,department) VALUES (?,?,?,?,?,?,?)",
            (username, email, generate_password_hash(password), full_name, role, "pending", department)
        )
        conn.commit()
    except Exception as e:
        conn.close()
        return jsonify({"error": "Username or email already exists"}), 409
    conn.close()

    return jsonify({"message": "Registration successful. Waiting for admin approval.", "status": "pending"}), 201


@app.route("/api/users/pending", methods=["GET"])
@require_role('admin')
def pending_users():
    conn = get_db()
    users = conn.execute("SELECT id,username,email,full_name,role,department FROM users WHERE status='pending'").fetchall()
    conn.close()
    return jsonify([dict(u) for u in users])


@app.route("/api/users/<int:user_id>/approve", methods=["POST"])
@require_role('admin')
def approve_user(user_id):
    conn = get_db()
    conn.execute("UPDATE users SET status='approved' WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User approved"})


@app.route("/api/users/<int:user_id>/reject", methods=["POST"])
@require_role('admin')
def reject_user(user_id):
    conn = get_db()
    conn.execute("UPDATE users SET status='rejected' WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "User rejected"})


@app.route("/api/users", methods=["GET"])
def list_users():
    conn = get_db()
    users = conn.execute("SELECT id,username,email,full_name,role,status,department FROM users").fetchall()
    conn.close()
    return jsonify([dict(u) for u in users])


@app.route("/api/courses", methods=["GET"])
def list_courses():
    conn = get_db()
    courses = conn.execute("""
        SELECT c.*, u.full_name as trainer_name
        FROM courses c LEFT JOIN users u ON c.trainer_id = u.id
    """).fetchall()
    conn.close()
    return jsonify([dict(c) for c in courses])


@app.route("/api/courses/<int:course_id>/modules", methods=["GET"])
def course_modules(course_id):
    conn = get_db()
    modules = conn.execute("SELECT * FROM modules WHERE course_id=? ORDER BY sort_order", (course_id,)).fetchall()
    result = []
    for m in modules:
        lessons = conn.execute("SELECT * FROM lessons WHERE module_id=? ORDER BY sort_order", (m["id"],)).fetchall()
        result.append({**dict(m), "lessons": [dict(l) for l in lessons]})
    conn.close()
    return jsonify(result)


@app.route("/api/enrollments/<int:user_id>", methods=["GET"])
def user_enrollments(user_id):
    conn = get_db()
    enrollments = conn.execute("""
        SELECT e.*, c.title, c.category, c.difficulty
        FROM enrollments e JOIN courses c ON e.course_id = c.id
        WHERE e.user_id=?
    """, (user_id,)).fetchall()
    conn.close()
    return jsonify([dict(e) for e in enrollments])


@app.route("/api/enroll", methods=["POST"])
def enroll():
    data = request.json
    user_id = data.get("user_id")
    course_id = data.get("course_id")
    conn = get_db()
    try:
        conn.execute("INSERT INTO enrollments (user_id,course_id) VALUES (?,?)", (user_id, course_id))
        conn.commit()
    except Exception:
        conn.close()
        return jsonify({"error": "Already enrolled"}), 409
    conn.close()
    return jsonify({"message": "Enrolled successfully"})


@app.route("/api/quizzes/<int:course_id>", methods=["GET"])
def get_quiz(course_id):
    conn = get_db()
    quiz = conn.execute("SELECT * FROM quizzes WHERE course_id=?", (course_id,)).fetchone()
    if not quiz:
        conn.close()
        return jsonify({"error": "No quiz found"}), 404
    questions = conn.execute("SELECT * FROM quiz_questions WHERE quiz_id=?", (quiz["id"],)).fetchall()
    conn.close()
    q_list = []
    for q in questions:
        q_list.append({
            "id": q["id"],
            "question": q["question"],
            "options": q["options"],
            "explanation": q["explanation"]
        })
    return jsonify({"quiz": dict(quiz), "questions": q_list})


@app.route("/api/quizzes/submit", methods=["POST"])
def submit_quiz():
    data = request.json
    user_id = data.get("user_id")
    quiz_id = data.get("quiz_id")
    answers = data.get("answers", [])

    conn = get_db()
    questions = conn.execute("SELECT * FROM quiz_questions WHERE quiz_id=?", (quiz_id,)).fetchall()
    correct = 0
    total = len(questions)
    results = []

    for i, q in enumerate(questions):
        user_ans = answers[i] if i < len(answers) else -1
        is_correct = user_ans == q["correct_index"]
        if is_correct:
            correct += 1
        results.append({
            "question": q["question"],
            "your_answer": user_ans,
            "correct_answer": q["correct_index"],
            "is_correct": is_correct,
            "explanation": q["explanation"]
        })

    score = (correct / total * 100) if total > 0 else 0
    conn.execute("INSERT INTO quiz_attempts (user_id,quiz_id,score,answers) VALUES (?,?,?,?)",
                 (user_id, quiz_id, score, str(answers)))
    conn.commit()
    conn.close()

    return jsonify({
        "score": round(score, 1),
        "correct": correct,
        "total": total,
        "passed": score >= 60,
        "results": results
    })


@app.route("/api/progress/<int:user_id>", methods=["GET"])
def user_progress(user_id):
    conn = get_db()
    enrollments = conn.execute("""
        SELECT e.*, c.title FROM enrollments e
        JOIN courses c ON e.course_id = c.id WHERE e.user_id=?
    """, (user_id,)).fetchall()
    quiz_attempts = conn.execute("""
        SELECT qa.*, q.title as quiz_title FROM quiz_attempts qa
        JOIN quizzes q ON qa.quiz_id = q.id WHERE qa.user_id=?
        ORDER BY qa.rowid DESC
    """, (user_id,)).fetchall()
    projects = conn.execute("""
        SELECT p.*, c.title as course_title FROM projects p
        JOIN courses c ON p.course_id = c.id WHERE p.user_id=?
    """, (user_id,)).fetchall()
    conn.close()
    return jsonify({
        "enrollments": [dict(e) for e in enrollments],
        "quizzes": [dict(q) for q in quiz_attempts],
        "projects": [dict(p) for p in projects]
    })


@app.route("/api/announcements", methods=["GET"])
def announcements():
    conn = get_db()
    anns = conn.execute("SELECT * FROM announcements ORDER BY rowid DESC").fetchall()
    conn.close()
    return jsonify([dict(a) for a in anns])


@app.route("/api/chat/history/<int:user_id>", methods=["GET"])
def chat_history(user_id):
    conn = get_db()
    messages = conn.execute(
        "SELECT role,message,created_at FROM chat_history WHERE user_id=? ORDER BY created_at DESC LIMIT 50",
        (user_id,)
    ).fetchall()
    conn.close()
    return jsonify([dict(m) for m in reversed(messages)])


# ─── Astra FULL endpoints ───
QUIZ_SESSIONS = {}


def cleanup_quiz_sessions():
    """Remove quiz sessions older than 30 minutes."""
    now = time.time()
    expired = [sid for sid, s in QUIZ_SESSIONS.items() if now - s.get('created_at', 0) > 1800]
    for sid in expired:
        del QUIZ_SESSIONS[sid]


def ensure_extra_tables():
    pass


@app.route("/api/notes", methods=["GET", "POST"])
def notes_api():
    if request.method == "GET":
        user_id = request.args.get("user_id", type=int)
        conn = get_db()
        rows = conn.execute("SELECT * FROM notes WHERE user_id=? ORDER BY rowid DESC", (user_id,)).fetchall()
        conn.close()
        return jsonify([dict(r) for r in rows])
    data = request.json or {}
    conn = get_db()
    conn.execute("INSERT INTO notes (user_id,lesson_id,course_id,title,content,tags) VALUES (?,?,?,?,?,?)",
                 (data.get("user_id"), data.get("lesson_id"), data.get("course_id"),
                  data.get("title", "Untitled"), data.get("content", ""), json.dumps(data.get("tags", []))))
    conn.commit()
    nid = conn.execute("SELECT last_insert_rowid() AS id").fetchone()["id"]
    conn.close()
    return jsonify({"id": nid, "message": "Note saved"}), 201


@app.route("/api/notes/<int:nid>", methods=["DELETE"])
def delete_note(nid):
    conn = get_db()
    conn.execute("DELETE FROM notes WHERE id=?", (nid,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Note deleted"})


@app.route("/api/notes/generate", methods=["POST"])
def notes_generate():
    from astra_engine import find_best_topic
    data = request.json or {}
    topic = data.get("topic", "")
    depth = data.get("depth", "detailed")
    tk, sk = find_best_topic(topic)
    if not tk:
        return jsonify({"error": "Unknown topic. Try Python, ML, React, Cloud, or Security."}), 404
    text = synthesize_notes(tk, sk, depth)
    return jsonify({"topic": topic, "notes": text})


@app.route("/api/flashcards", methods=["POST"])
def flashcards_api():
    from astra_engine import find_best_topic
    data = request.json or {}
    tk, sk = find_best_topic(data.get("topic", ""))
    if not tk:
        return jsonify({"error": "Unknown topic."}), 404
    _txt, cards = flashcards(tk, sk, int(data.get("count", 6)))
    return jsonify({"cards": cards})


@app.route("/api/learning-path", methods=["POST"])
def learning_path_api():
    from astra_engine import get_user_context
    data = request.json or {}
    ctx = get_user_context(data.get("user_id")) if data.get("user_id") else None
    return jsonify({"path": learning_path(data.get("goal", "python"), ctx)})


@app.route("/api/quiz/session/start", methods=["POST"])
def quiz_start():
    cleanup_quiz_sessions()
    from astra_engine import QUIZ_BANK
    data = request.json or {}
    bank = []
    for qs in QUIZ_BANK.values():
        bank.extend(qs)
    random = __import__("random")
    random.shuffle(bank)
    questions = bank[: int(data.get("count", 5))]
    sid = str(uuid.uuid4())
    QUIZ_SESSIONS[sid] = {
        "questions": questions,
        "index": 0,
        "correct": 0,
        "answers": [],
        "course_id": data.get("course_id"),
        "created_at": time.time()
    }
    q = questions[0]
    return jsonify({"session_id": sid, "index": 0, "total": len(questions),
                    "question": q["q"], "options": q["opts"]})


@app.route("/api/quiz/session/answer", methods=["POST"])
def quiz_answer():
    cleanup_quiz_sessions()
    data = request.json or {}
    sess = QUIZ_SESSIONS.get(data.get("session_id"))
    if not sess:
        return jsonify({"error": "Invalid session"}), 404
    i = sess["index"]
    q = sess["questions"][i]
    user_ans = int(data.get("answer", -1))
    ok = user_ans == q["ans"]
    if ok:
        sess["correct"] += 1
    sess["answers"].append({"q": q["q"], "your": user_ans, "correct": q["ans"], "ok": ok, "exp": q["exp"]})
    feedback = f"{'Correct! ' if ok else 'Not quite. '}{q['exp']}"
    sess["index"] += 1
    if sess["index"] >= len(sess["questions"]):
        total = len(sess["questions"])
        score = round(sess["correct"] / total * 100, 1)
        uid = data.get("user_id")
        if uid:
            conn = get_db()
            course_id = sess.get('course_id')
            if course_id:
                quiz = conn.execute("SELECT id FROM quizzes WHERE course_id=?", (course_id,)).fetchone()
            else:
                quiz = conn.execute("SELECT id FROM quizzes LIMIT 1").fetchone()
            if quiz:
                conn.execute("INSERT INTO quiz_attempts (user_id,quiz_id,score,answers) VALUES (?,?,?,?)",
                             (uid, quiz["id"], score, json.dumps(sess["answers"])))
                conn.commit()
            conn.close()
        done = dict(sess)
        del QUIZ_SESSIONS[data.get("session_id")]

        # Record spaced repetition reviews
        try:
            from spaced_repetition import record_review, init_spaced_tables
            init_spaced_tables()
            for a in done["answers"]:
                # Extract a concept key from the question text
                concept_key = a["q"][:50].lower().replace(" ", "_")
                record_review(uid or 0, concept_key, 1.0 if a["ok"] else 0.0)
        except Exception:
            pass  # Don't break quiz if spaced repetition fails

        weak = [a for a in done["answers"] if not a["ok"]]
        nxt = "Say 'flashcards' to revise missed topics, or 'quiz me' for another round."
        if weak:
            nxt = f"Revise: {', '.join(a['q'][:50] for a in weak[:2])}. " + nxt
        return jsonify({"done": True, "score": score, "correct": done["correct"],
                        "total": total, "feedback": feedback, "next": nxt, "answers": done["answers"]})
    nq = sess["questions"][sess["index"]]
    return jsonify({"done": False, "feedback": feedback, "index": sess["index"],
                    "total": len(sess["questions"]), "question": nq["q"], "options": nq["opts"]})


@app.route("/api/reviews/due/<int:user_id>", methods=["GET"])
def due_reviews(user_id):
    try:
        from spaced_repetition import get_due_reviews, get_weak_concepts, init_spaced_tables
        init_spaced_tables()
        due = get_due_reviews(user_id)
        weak = get_weak_concepts(user_id)
        return jsonify({"due_reviews": due, "weak_concepts": weak})
    except Exception as e:
        return jsonify({"due_reviews": [], "weak_concepts": [], "error": str(e)})


@app.route("/api/pdf/study-guide", methods=["POST"])
def pdf_guide():
    from astra_engine import find_best_topic
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    data = request.json or {}
    topic = data.get("topic", "Python")
    tk, sk = find_best_topic(topic)
    if not tk:
        return jsonify({"error": "Unknown topic."}), 404
    text = synthesize_notes(tk, sk, data.get("depth", "detailed"))
    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, title=f"Astra Study Guide - {topic}")
    styles = getSampleStyleSheet()
    story = [Paragraph(f"Astra Study Guide — {topic}", styles["Title"]), Spacer(1, 12)]
    for line in text.split("\n"):
        s = line.strip()
        if not s:
            story.append(Spacer(1, 6))
        elif s.startswith("# "):
            story.append(Paragraph(s[2:], styles["Heading1"]))
        elif s.startswith("## "):
            story.append(Paragraph(s[3:], styles["Heading2"]))
        else:
            story.append(Paragraph(s.replace("`", "").replace("**", "")[:500], styles["BodyText"]))
    doc.build(story)
    buf.seek(0)
    return Response(buf.read(), mimetype="application/pdf",
                    headers={"Content-Disposition": f"attachment; filename=astra-guide-{tk}.pdf"})


@app.route("/api/search", methods=["GET"])
def search_api():
    q = f"%{request.args.get('q', '')}%"
    conn = get_db()
    courses = conn.execute("SELECT * FROM courses WHERE title LIKE ? OR description LIKE ? LIMIT 10", (q, q)).fetchall()
    lessons = conn.execute("SELECT l.*, m.title AS module_title FROM lessons l JOIN modules m ON l.module_id=m.id "
                           "WHERE l.title LIKE ? OR l.content LIKE ? LIMIT 10", (q, q)).fetchall()
    conn.close()
    return jsonify({"courses": [dict(c) for c in courses], "lessons": [dict(l) for l in lessons]})


@app.route("/api/profile/<int:user_id>", methods=["GET"])
def profile_api(user_id):
    from astra_engine import get_user_context
    ctx = get_user_context(user_id)
    if not ctx:
        return jsonify({"error": "User not found"}), 404
    ctx["user"].pop("password_hash", None)
    conn = get_db()
    pref = conn.execute("SELECT * FROM user_preferences WHERE user_id=?", (user_id,)).fetchone()
    notes = conn.execute("SELECT id,title FROM notes WHERE user_id=? ORDER BY rowid DESC LIMIT 10", (user_id,)).fetchall()
    conn.close()
    ctx["preferences"] = dict(pref) if pref else {"skill_level": "intermediate", "depth": "standard"}
    ctx["notes"] = [dict(n) for n in notes]
    return jsonify(ctx)


@app.route("/api/preferences", methods=["POST"])
def prefs_api():
    data = request.json or {}
    conn = get_db()
    conn.execute("INSERT OR REPLACE INTO user_preferences (user_id,skill_level,depth) VALUES (?,?,?)",
                 (data.get("user_id"), data.get("skill_level", "intermediate"), data.get("depth", "standard")))
    conn.commit()
    conn.close()
    return jsonify({"message": "Preferences saved"})


@app.route("/api/chat/feedback", methods=["POST"])
def feedback_api():
    data = request.json or {}
    conn = get_db()
    conn.execute("INSERT INTO chat_feedback (user_id,session_id,message_index,rating) VALUES (?,?,?,?)",
                 (data.get("user_id", 0), data.get("session_id", ""), data.get("message_index", 0), data.get("rating", "")))
    conn.commit()
    conn.close()
    return jsonify({"message": "Feedback recorded"})


@app.route("/api/chat/export", methods=["GET"])
def export_api():
    uid = request.args.get("user_id", type=int, default=0)
    sid = request.args.get("session_id", default="")
    conn = get_db()
    rows = conn.execute("SELECT role,message,created_at FROM chat_history WHERE user_id=? AND session_id=? ORDER BY rowid",
                        (uid, sid)).fetchall()
    conn.close()
    lines = ["# Astra Chat Export\n"]
    for r in rows:
        who = "You" if r["role"] == "user" else "Astra"
        lines.append(f"**{who}:** {r['message']}\n")
    return Response("\n".join(lines), mimetype="text/markdown",
                    headers={"Content-Disposition": "attachment; filename=astra-chat.md"})


@app.route("/api/chat/clear", methods=["POST"])
def clear_api():
    data = request.json or {}
    conn = get_db()
    conn.execute("DELETE FROM chat_history WHERE user_id=? AND session_id=?",
                 (data.get("user_id", 0), data.get("session_id", "")))
    conn.commit()
    conn.close()
    return jsonify({"message": "Chat cleared"})


@app.route("/api/lessons/<int:lesson_id>/complete", methods=["POST"])
def complete_lesson(lesson_id):
    data = request.json or {}
    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"error": "user_id required"}), 400
    
    conn = get_db()
    # Mark lesson complete
    conn.execute("INSERT OR REPLACE INTO lesson_progress (user_id, lesson_id, completed) VALUES (?, ?, 1)",
                 (user_id, lesson_id))
    
    # Recalculate course progress
    lesson = conn.execute("SELECT m.course_id FROM lessons l JOIN modules m ON l.module_id = m.id WHERE l.id=?", (lesson_id,)).fetchone()
    if lesson:
        course_id = lesson["course_id"]
        total = conn.execute("SELECT COUNT(*) as cnt FROM lessons l JOIN modules m ON l.module_id = m.id WHERE m.course_id=?", (course_id,)).fetchone()["cnt"]
        done = conn.execute("SELECT COUNT(*) as cnt FROM lesson_progress lp JOIN lessons l ON lp.lesson_id = l.id JOIN modules m ON l.module_id = m.id WHERE m.course_id=? AND lp.user_id=? AND lp.completed=1", (course_id, user_id)).fetchone()["cnt"]
        pct = round((done / total) * 100, 1) if total > 0 else 0
        completed = 1 if pct >= 100 else 0
        conn.execute("UPDATE enrollments SET progress_pct=?, completed=? WHERE user_id=? AND course_id=?",
                     (pct, completed, user_id, course_id))
    
    conn.commit()
    conn.close()
    return jsonify({"message": "Lesson completed", "progress": pct if lesson else 0})


# Initialize database tables on server startup (works for both direct execution and gunicorn)
init_db()
seed_demo_data()
ensure_extra_tables()
try:
    from spaced_repetition import init_spaced_tables
    init_spaced_tables()
except Exception:
    pass

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port, threaded=True)
