import sqlite3
import os
import shutil

ORIGINAL_DB_PATH = os.path.join(os.path.dirname(__file__), "capacity_connect.db")

if os.environ.get("VERCEL"):
    DB_PATH = "/tmp/capacity_connect.db"
    if not os.path.exists(DB_PATH) and os.path.exists(ORIGINAL_DB_PATH):
        try:
            shutil.copy2(ORIGINAL_DB_PATH, DB_PATH)
        except Exception as e:
            print(f"Error copying DB to /tmp: {e}")
else:
    DB_PATH = ORIGINAL_DB_PATH

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        full_name TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'trainee',
        status TEXT NOT NULL DEFAULT 'pending',
        department TEXT DEFAULT ''
    );
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        difficulty TEXT DEFAULT 'beginner',
        trainer_id INTEGER,
        FOREIGN KEY (trainer_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS modules (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT DEFAULT '',
        sort_order INTEGER DEFAULT 0,
        FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS lessons (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        module_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        content_type TEXT DEFAULT 'text',
        sort_order INTEGER DEFAULT 0,
        duration_minutes INTEGER DEFAULT 10,
        FOREIGN KEY (module_id) REFERENCES modules(id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS enrollments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        completed INTEGER DEFAULT 0,
        progress_pct REAL DEFAULT 0.0,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (course_id) REFERENCES courses(id),
        UNIQUE(user_id, course_id)
    );
    CREATE TABLE IF NOT EXISTS lesson_progress (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        lesson_id INTEGER NOT NULL,
        completed INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (lesson_id) REFERENCES lessons(id),
        UNIQUE(user_id, lesson_id)
    );
    CREATE TABLE IF NOT EXISTS quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT DEFAULT '',
        passing_score REAL DEFAULT 60.0,
        FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS quiz_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quiz_id INTEGER NOT NULL,
        question TEXT NOT NULL,
        options TEXT NOT NULL,
        correct_index INTEGER NOT NULL,
        explanation TEXT DEFAULT '',
        FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS quiz_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        quiz_id INTEGER NOT NULL,
        score REAL NOT NULL,
        answers TEXT DEFAULT '[]',
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
    );
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT DEFAULT '',
        status TEXT DEFAULT 'submitted',
        trainer_feedback TEXT DEFAULT '',
        grade TEXT DEFAULT '',
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    );
    CREATE TABLE IF NOT EXISTS certificates (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        certificate_id TEXT UNIQUE NOT NULL,
        issued_at TEXT DEFAULT (datetime('now')),
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (course_id) REFERENCES courses(id)
    );
    CREATE TABLE IF NOT EXISTS announcements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        posted_by INTEGER,
        target_role TEXT DEFAULT 'all',
        FOREIGN KEY (posted_by) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS chat_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        session_id TEXT NOT NULL,
        role TEXT NOT NULL,
        message TEXT NOT NULL,
        metadata TEXT DEFAULT '{}',
        created_at TEXT DEFAULT (datetime('now')),
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        lesson_id INTEGER,
        course_id INTEGER,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        tags TEXT DEFAULT '[]',
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS user_preferences (
        user_id INTEGER PRIMARY KEY,
        skill_level TEXT DEFAULT 'intermediate',
        depth TEXT DEFAULT 'standard',
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    CREATE TABLE IF NOT EXISTS chat_feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        session_id TEXT NOT NULL,
        message_index INTEGER DEFAULT 0,
        rating TEXT NOT NULL,
        created_at TEXT DEFAULT (datetime('now'))
    );
    """)
    conn.commit()
    conn.close()


def seed_demo_data():
    conn = get_db()
    c = conn.cursor()
    if c.execute("SELECT COUNT(*) FROM users").fetchone()[0] > 0:
        conn.close()
        return
    from werkzeug.security import generate_password_hash
    users = [
        ("admin", "admin@gov.in", generate_password_hash("admin123"), "Dr. Rajesh Kumar", "admin", "approved", "Administration"),
        ("trainer_priya", "priya@gov.in", generate_password_hash("trainer123"), "Priya Sharma", "trainer", "approved", "CS"),
        ("trainer_ankit", "ankit@gov.in", generate_password_hash("trainer123"), "Ankit Verma", "trainer", "approved", "DS"),
        ("mourya", "mourya@gov.in", generate_password_hash("mourya123"), "Mourya", "trainee", "approved", "AI & Data Science"),
        ("learner", "learner@gov.in", generate_password_hash("learner123"), "Learner", "trainee", "approved", "Digital Skills"),
        ("sneha", "sneha@gov.in", generate_password_hash("trainee123"), "Sneha Patel", "trainee", "approved", "CS"),
        ("rahul", "rahul@gov.in", generate_password_hash("trainee123"), "Rahul Gupta", "trainee", "approved", "DS"),
        ("meera", "meera@gov.in", generate_password_hash("trainee123"), "Meera Singh", "trainee", "approved", "CS"),
    ]
    c.executemany("INSERT INTO users (username,email,password_hash,full_name,role,status,department) VALUES (?,?,?,?,?,?,?)", users)

    courses = [
        ("Python for Data Science", "Master Python from basics to ML pipelines.", "Data Science", "beginner", 3),
        ("Machine Learning Fundamentals", "Supervised, unsupervised, and reinforcement learning.", "Data Science", "intermediate", 3),
        ("Web Development with React", "Build modern responsive web apps with React.", "Web Development", "beginner", 2),
        ("Cloud Computing with AWS", "Deploy and scale on Amazon Web Services.", "Cloud", "intermediate", 2),
        ("Cybersecurity Essentials", "Ethical hacking, network security, threat analysis.", "Security", "beginner", 2),
    ]
    c.executemany("INSERT INTO courses (title,description,category,difficulty,trainer_id) VALUES (?,?,?,?,?)", courses)

    modules = [
        (1, "Python Basics", "Variables, loops, functions", 1),
        (1, "Data Handling", "NumPy, Pandas, DataFrames", 2),
        (1, "Visualization", "Matplotlib, Seaborn", 3),
        (2, "Supervised Learning", "Regression, Classification", 1),
        (2, "Unsupervised Learning", "Clustering, Dimensionality Reduction", 2),
        (3, "React Fundamentals", "Components, JSX, State, Props", 1),
        (3, "Advanced React", "Hooks, Context, Routing", 2),
        (4, "AWS Core Services", "EC2, S3, IAM", 1),
        (5, "Network Security", "Firewalls, IDS/IPS", 1),
        (5, "Ethical Hacking", "Penetration testing basics", 2),
    ]
    c.executemany("INSERT INTO modules (course_id,title,description,sort_order) VALUES (?,?,?,?)", modules)

    lessons = [
        (1, "What is Python?", "Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991.\n\nKey characteristics:\n- Easy to learn syntax\n- Dynamic typing\n- Extensive standard library\n- Cross-platform\n- Large community support\n\nPython is used in web development, data science, AI, automation, and more.", "text", 1, 15),
        (1, "Variables and Data Types", "Variables in Python are names that reference values. No need to declare types explicitly.\n\n# Strings\nname = 'Capacity Connect'\n\n# Integers\ncount = 42\n\n# Floats\ntemperature = 36.6\n\n# Booleans\nis_active = True\n\n# Lists\nmodules = ['Basics', 'Data', 'ML']\n\n# Dictionaries\ncourse = {'title': 'Python', 'level': 'beginner'}", "text", 2, 20),
        (1, "Control Flow", "Python uses if/elif/else for conditionals and for/while for loops.\n\n# If statement\nscore = 85\nif score >= 90:\n    grade = 'A'\nelif score >= 80:\n    grade = 'B'\nelse:\n    grade = 'C'\n\n# For loop\nfor i in range(5):\n    print(i)\n\n# While loop\nwhile count > 0:\n    count -= 1", "text", 3, 20),
        (1, "Functions", "Functions are reusable blocks of code defined with 'def'.\n\ndef greet(name):\n    return f'Hello, {name}!'\n\n# Default parameters\ndef add(a, b=0):\n    return a + b\n\n# Lambda functions\ndouble = lambda x: x * 2\n\n# *args and **kwargs\ndef flexible(*args, **kwargs):\n    print(args, kwargs)", "text", 4, 20),
        (2, "Introduction to NumPy", "NumPy is the foundation of numerical computing in Python.\n\nimport numpy as np\n\n# Creating arrays\narr = np.array([1, 2, 3, 4, 5])\nmatrix = np.array([[1,2],[3,4]])\n\n# Operations\nprint(arr.mean())\nprint(arr.std())\nprint(matrix.dot(matrix))\n\n# Broadcasting\narr * 2  # element-wise multiplication", "text", 1, 25),
        (2, "Pandas DataFrames", "Pandas provides DataFrame for structured data manipulation.\n\nimport pandas as pd\n\ndf = pd.DataFrame({\n    'name': ['Sneha', 'Rahul'],\n    'score': [92, 85]\n})\n\n# Filtering\ndf[df['score'] > 85]\n\n# Grouping\ndf.groupby('dept').mean()\n\n# Missing data\ndf.fillna(0)\ndf.dropna()", "text", 2, 25),
        (3, "Matplotlib Basics", "Matplotlib is Python's primary plotting library.\n\nimport matplotlib.pyplot as plt\n\n# Line plot\nplt.plot([1,2,3], [4,5,6])\nplt.title('Sales Trend')\nplt.xlabel('Month')\nplt.ylabel('Revenue')\nplt.show()\n\n# Bar chart\nplt.bar(['A','B','C'], [10,20,15])\nplt.show()\n\n# Histogram\nplt.hist(data, bins=30)\nplt.show()", "text", 1, 20),
        (4, "What is Machine Learning?", "Machine Learning is a subset of AI where systems learn patterns from data to make predictions or decisions without being explicitly programmed.\n\nTypes:\n1. Supervised Learning - labeled data (regression, classification)\n2. Unsupervised Learning - unlabeled data (clustering, reduction)\n3. Reinforcement Learning - learning through rewards/penalties\n\nThe ML Pipeline:\nData Collection -> Preprocessing -> Feature Engineering -> Model Training -> Evaluation -> Deployment", "text", 1, 15),
        (4, "Linear Regression", "Linear Regression models the relationship between variables by fitting a linear equation.\n\ny = mx + b\n\nwhere:\n- y = dependent variable\n- x = independent variable\n- m = slope (coefficient)\n- b = intercept\n\nfrom sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\npredictions = model.predict(X_test)\n\nEvaluation metrics: R-squared, MAE, RMSE", "text", 2, 25),
        (5, "Decision Trees", "Decision trees split data based on feature values to make predictions.\n\nfrom sklearn.tree import DecisionTreeClassifier\ntree = DecisionTreeClassifier(max_depth=5)\ntree.fit(X_train, y_train)\n\nAdvantages:\n- Easy to interpret\n- No feature scaling needed\n- Handles mixed data types\n\nDisadvantages:\n- Prone to overfitting\n- Unstable with small data changes\n\nSolution: Use Random Forests (ensemble of trees)", "text", 1, 20),
        (6, "React Components", "React apps are built from components - reusable UI pieces.\n\nfunction Welcome({ name }) {\n  return <h1>Hello, {name}!</h1>;\n}\n\n// JSX is a syntax extension\nconst element = (\n  <div>\n    <Welcome name=\"Sneha\" />\n    <Welcome name=\"Rahul\" />\n  </div>\n);\n\nComponents can be:\n- Functional (preferred)\n- Class-based (legacy)", "text", 1, 20),
        (6, "State and Props", "Props pass data parent-to-child. State manages internal component data.\n\nimport { useState } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n  return (\n    <div>\n      <p>Count: {count}</p>\n      <button onClick={() => setCount(count + 1)}>\n        Increment\n      </button>\n    </div>\n  );\n}\n\nRules:\n- Props are read-only\n- State is mutable via setState\n- State updates trigger re-renders", "text", 2, 20),
        (7, "React Hooks", "Hooks let you use state and lifecycle in functional components.\n\nimport { useState, useEffect, useContext } from 'react';\n\nfunction UserProfile({ userId }) {\n  const [user, setUser] = useState(null);\n  \n  useEffect(() => {\n    fetchUser(userId).then(setUser);\n  }, [userId]);\n  \n  if (!user) return <Spinner />;\n  return <div>{user.name}</div>;\n}\n\nCommon hooks: useState, useEffect, useContext, useRef, useMemo", "text", 1, 25),
        (8, "AWS EC2 and S3", "EC2 provides virtual servers. S3 provides object storage.\n\n# EC2 Instance\nez2 = boto3.resource('ec2')\ninstances = ec2.create_instances(\n    ImageId='ami-xxx',\n    InstanceType='t2.micro',\n    MinCount=1, MaxCount=1\n)\n\n# S3 Bucket\ns3 = boto3.client('s3')\ns3.create_bucket(Bucket='my-bucket')\ns3.upload_file('file.txt', 'my-bucket', 'file.txt')\n\nIAM controls access. Security Groups control network.", "text", 1, 20),
        (9, "Network Security Basics", "Network security protects data in transit and at rest.\n\nKey concepts:\n- Firewall: Filters incoming/outgoing traffic\n- IDS/IPS: Detects/prevents intrusions\n- VPN: Encrypted tunnel for remote access\n- SSL/TLS: Encrypts web traffic\n\nCommon attacks:\n- DDoS: Overwhelms servers\n- Man-in-the-middle: Intercepts communications\n- SQL Injection: Malicious database queries\n- XSS: Injects scripts into web pages\n\nDefense: Layered security (defense in depth)", "text", 1, 20),
        (10, "Penetration Testing Basics", "Penetration testing simulates attacks to find vulnerabilities.\n\nPhases:\n1. Reconnaissance - Gather information\n2. Scanning - Find open ports/services\n3. Exploitation - Attempt to breach\n4. Post-Exploitation - Maintain access\n5. Reporting - Document findings\n\nTools:\n- Nmap: Network scanning\n- Metasploit: Exploitation framework\n- Burp Suite: Web app testing\n- Wireshark: Packet analysis\n\nAlways get written permission before testing.", "text", 1, 25),
    ]
    c.executemany("INSERT INTO lessons (module_id,title,content,content_type,sort_order,duration_minutes) VALUES (?,?,?,?,?,?)", lessons)

    enrollments = [
        (4, 1, 0, 60.0), (4, 3, 0, 30.0), (5, 2, 0, 45.0),
        (5, 1, 0, 80.0), (6, 1, 0, 100.0), (6, 4, 0, 20.0),
    ]
    c.executemany("INSERT INTO enrollments (user_id,course_id,completed,progress_pct) VALUES (?,?,?,?)", enrollments)

    quizzes = [
        (1, "Python Basics Quiz", "Test your Python fundamentals", 60.0),
        (2, "ML Foundations Quiz", "Check your ML understanding", 60.0),
        (3, "React Basics Quiz", "React knowledge check", 60.0),
    ]
    c.executemany("INSERT INTO quizzes (course_id,title,description,passing_score) VALUES (?,?,?,?)", quizzes)

    import json
    q1_questions = [
        (1, "What is the output of: print(type(42))?", json.dumps(["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'number'>"]), 0, "42 is an integer literal, so Python creates an int object."),
        (1, "Which keyword is used to define a function in Python?", json.dumps(["func", "function", "def", "define"]), 2, "'def' is the keyword used to define functions in Python."),
        (1, "What does 'len()' do?", json.dumps(["Calculates length", "Converts to list", "Prints output", "Creates loop"]), 0, "len() returns the number of items in an object."),
        (1, "Which data type is immutable in Python?", json.dumps(["List", "Dictionary", "Set", "Tuple"]), 3, "Tuples cannot be modified after creation, unlike lists."),
        (1, "What is the correct file extension for Python files?", json.dumps([".python", ".py", ".pt", ".pyt"]), 1, "Python files use the .py extension."),
    ]
    c.executemany("INSERT INTO quiz_questions (quiz_id,question,options,correct_index,explanation) VALUES (?,?,?,?,?)", q1_questions)

    q2_questions = [
        (2, "What type of learning uses labeled data?", json.dumps(["Unsupervised", "Supervised", "Reinforcement", "Semi-supervised"]), 1, "Supervised learning trains on labeled input-output pairs."),
        (2, "What is overfitting?", json.dumps(["Model too simple", "Model memorizes training data", "Model is fast", "Model uses too little data"]), 1, "Overfitting means the model performs well on training data but poorly on new data."),
        (2, "Which metric measures classification accuracy?", json.dumps(["MSE", "R-squared", "Accuracy Score", "MAE"]), 2, "Accuracy Score measures the proportion of correct predictions."),
        (2, "What does a Decision Tree do?", json.dumps(["Clusters data", "Splits data by feature values", "Averages data", "Generates random data"]), 1, "Decision trees recursively split data based on feature values to make predictions."),
    ]
    c.executemany("INSERT INTO quiz_questions (quiz_id,question,options,correct_index,explanation) VALUES (?,?,?,?,?)", q2_questions)

    q3_questions = [
        (3, "What is JSX?", json.dumps(["A database", "JavaScript XML syntax extension", "A CSS framework", "A testing tool"]), 1, "JSX lets you write HTML-like syntax in JavaScript for React components."),
        (3, "Which hook manages state in functional components?", json.dumps(["useEffect", "useState", "useContext", "useRef"]), 1, "useState returns a state value and a setter function."),
        (3, "Props in React are:", json.dumps(["Mutable", "Read-only", "Global", "Optional"]), 1, "Props flow from parent to child and are read-only."),
    ]
    c.executemany("INSERT INTO quiz_questions (quiz_id,question,options,correct_index,explanation) VALUES (?,?,?,?,?)", q3_questions)

    announcements = [
        ("Welcome to Capacity Connect!", "Government of Odisha's digital capacity building portal is now live. Start learning today.", 1, "all"),
        ("New Course: AI Fundamentals", "A new course on Artificial Intelligence has been added. Enroll now!", 1, "trainee"),
        ("Project Submission Deadline", "All project submissions for Web Development are due by end of month.", 1, "trainee"),
    ]
    c.executemany("INSERT INTO announcements (title,content,posted_by,target_role) VALUES (?,?,?,?)", announcements)

    projects = [
        (4, 1, "Data Analysis Project", "approved", "Excellent work on data visualization!", "A"),
        (5, 2, "ML Model Build", "submitted", "", ""),
        (6, 1, "Python Automation Script", "revision", "Please add error handling and documentation.", "B"),
    ]
    c.executemany("INSERT INTO projects (user_id,course_id,title,status,trainer_feedback,grade) VALUES (?,?,?,?,?,?)", projects)

    conn.commit()
    conn.close()
