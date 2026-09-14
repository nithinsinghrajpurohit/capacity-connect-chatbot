import json
import random
import re
from database import get_db

# ─── Knowledge Base for topic teaching ───
TOPIC_KNOWLEDGE = {
    "python": {
        "keywords": ["python", "programming", "coding", "code", "function", "functions", "def", "method", "methods", "variable", "variables", "var", "vars", "loop", "loops", "list", "lists", "dictionary", "dictionaries", "string", "strings", "class", "classes", "object", "objects", "oop", "file", "error", "exception"],
        "topics": {
            "variables": {
                "title": "Python Variables",
                "what": "Variables are named containers that store data values. In Python, you don't need to declare the type explicitly.",
                "intuition": "Think of a variable as a labeled box. You put something inside and give it a name so you can find it later.",
                "example": "```python\nname = 'Astra'\nage = 25\npi = 3.14\nis_active = True\n```",
                "key_points": ["No type declaration needed", "Case-sensitive (age != Age)", "Assign with = sign"],
                "practice": "Try: Create a variable called 'course' with value 'Python' and print it.",
                "common_mistakes": ["Using = instead of == in conditions", "Using undefined variables", "Confusing variable names (myVar vs myvar)"]
            },
            "functions": {
                "title": "Python Functions",
                "what": "Functions are reusable blocks of code that perform a specific task. They take inputs (parameters) and return outputs.",
                "intuition": "A function is like a recipe. It has a name, takes ingredients (parameters), follows steps (code), and produces a dish (return value).",
                "example": "```python\ndef greet(name):\n    return f'Hello, {name}!'\n\nresult = greet('Sneha')\nprint(result)  # Hello, Sneha!\n```",
                "key_points": ["Defined with 'def' keyword", "Can have parameters", "Return statement sends back value", "Can be called multiple times"],
                "practice": "Write a function 'add' that takes two numbers and returns their sum.",
                "common_mistakes": ["Forgetting return statement", "Not calling the function", "Wrong indentation"]
            },
            "loops": {
                "title": "Python Loops",
                "what": "Loops repeat a block of code. Python has 'for' loops (iterating over sequences) and 'while' loops (repeating until condition is false).",
                "intuition": "A for loop is like going through a checklist item by item. A while loop is like keeping the lights on until you decide to switch them off.",
                "example": "```python\n# For loop\nfor i in range(5):\n    print(i)  # 0,1,2,3,4\n\n# While loop\ncount = 3\nwhile count > 0:\n    print(count)\n    count -= 1\n```",
                "key_points": ["for iterates over a sequence", "while checks condition each time", "range() generates numbers", "break exits loop, continue skips iteration"],
                "practice": "Write a loop that prints all even numbers from 1 to 20.",
                "common_mistakes": ["Infinite while loops (forgetting to update condition)", "Off-by-one errors with range()", "Modifying list while iterating"]
            },
            "data_types": {
                "title": "Python Data Types",
                "what": "Python has several built-in data types: int, float, str, bool, list, tuple, dict, set.",
                "intuition": "Different types of containers hold different things. A list is like a shelf, a dictionary is like a phone book, a string is like a sentence.",
                "example": "```python\nage = 25          # int\npi = 3.14         # float\nname = 'Astra'    # str\nactive = True     # bool\nitems = [1,2,3]   # list\ninfo = {'key':'val'} # dict\n```",
                "key_points": ["int: whole numbers", "float: decimal numbers", "str: text in quotes", "bool: True/False", "list: ordered, mutable collection", "dict: key-value pairs"],
                "practice": "Create a dictionary with course name, difficulty, and enrollment count.",
                "common_mistakes": ["Mixing types in operations", "Mutable default arguments", "Confusing = (assignment) with == (comparison)"]
            },
            "oop": {
                "title": "Object-Oriented Programming",
                "what": "OOP organizes software design around data, or objects, rather than functions and logic.",
                "intuition": "Think of a class as a blueprint for a house, and an object as the actual house built from that blueprint.",
                "example": "```python\nclass Dog:\n    def __init__(self, name):\n        self.name = name\n    def bark(self):\n        return 'Woof!'\n\nd = Dog('Rex')\nd.bark()\n```",
                "key_points": ["Classes and Objects", "Inheritance", "Encapsulation", "Polymorphism"],
                "practice": "Create a Car class with a start_engine method.",
                "common_mistakes": ["Forgetting self in method definitions", "Confusing class attributes and instance attributes"]
            },
            "file_handling": {
                "title": "File Handling",
                "what": "File handling allows Python to read from and write to files using the built-in open() function.",
                "intuition": "Like opening a physical book to read its contents or writing in a notebook, but done programmatically.",
                "example": "```python\nwith open('file.txt', 'r') as f:\n    content = f.read()\n\nwith open('out.txt', 'w') as f:\n    f.write('Hello')\n```",
                "key_points": ["Use 'with' context managers", "Modes: 'r' (read), 'w' (write), 'a' (append)", "Don't forget to close files if not using 'with'"],
                "practice": "Write a script that appends your name to a text file.",
                "common_mistakes": ["Forgetting to close the file", "Opening in 'w' mode instead of 'a' and erasing data", "File not found errors"]
            },
            "error_handling": {
                "title": "Error Handling",
                "what": "Error handling prevents your program from crashing when an error occurs, using try/except blocks.",
                "intuition": "Like having a backup plan. If plan A (try) fails, execute plan B (except) instead of giving up.",
                "example": "```python\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero!')\nfinally:\n    print('Done')\n```",
                "key_points": ["try block tests code", "except block handles errors", "finally executes regardless", "You can raise custom exceptions"],
                "practice": "Write a try/except block that catches a ValueError when converting 'abc' to int.",
                "common_mistakes": ["Catching all exceptions with a bare except", "Ignoring exceptions implicitly", "Putting too much code in try block"]
            }
        }
    },
    "artificial_intelligence": {
        "keywords": [
            "artificial intelligence", "ai", "artificial intelligence basics", "ai basics",
            "what is ai", "ani", "agi", "asi", "turing test", "expert system",
            "generative ai", "genai", "llm", "large language model",
            "computer vision", "nlp", "natural language processing", "robotics",
            "autonomous agent", "agentic ai"
        ],
        "topics": {
            "basics": {
                "title": "Artificial Intelligence (AI)",
                "what": "Artificial Intelligence (AI) is the broad branch of computer science dedicated to building machines and systems capable of performing tasks that typically require human intelligence, such as visual perception, speech recognition, natural language reasoning, planning, and autonomous decision-making.",
                "intuition": "Think of AI as building an artificial mind. While humans perceive the world through eyes and ears and use their brains to make decisions, an AI system ingests data (images, text, sensor streams), processes it through algorithms and neural networks, and produces intelligent actions or solutions.",
                "example": "AI Hierarchy & Core Disciplines:\n❯ Artificial Intelligence (Broadest Science): The overarching discipline of simulating human cognition (Logic, Search, Knowledge Graphs, Vision, NLP, Robotics)\n❯ Machine Learning (Subset of AI): Systems that learn patterns directly from data instead of hand-coded rules\n❯ Deep Learning (Subset of ML): Multi-layered neural networks inspired by the human brain\n❯ Generative AI & LLMs (Modern Frontier): Systems generating novel text, imagery, and code (e.g., GPT, Claude, Gemini)",
                "key_points": [
                    "AI is the parent discipline — Machine Learning is a subset, and Deep Learning is a specialized subset of ML",
                    "Three Capability Stages: Narrow AI (ANI - specialized tasks today), General AI (AGI - human-level across all domains), Super AI (ASI - exceeds human cognition)",
                    "Four Core Pillars: Perception (Computer Vision/Speech), Reasoning & Planning (Logic/Search), Learning (ML/DL), Action (Robotics/Autonomous Agents)",
                    "Transformative Real-World Applications: Autonomous navigation, Medical diagnostics, Natural language assistants, Algorithmic discovery, Smart manufacturing"
                ],
                "practice": "Explain the difference between Narrow AI (ANI) and Artificial General Intelligence (AGI) with an example of each.",
                "common_mistakes": [
                    "Confusing AI with Machine Learning (AI is the entire science; ML is just one methodology within it)",
                    "Believing current AI is conscious or has intent (modern AI is sophisticated mathematical pattern processing)",
                    "Thinking AI requires deep learning (classical AI includes symbolic logic, A* search, and expert systems)"
                ]
            },
            "types": {
                "title": "Types & Capabilities of AI",
                "what": "AI is classified by capability into Narrow AI (ANI), General AI (AGI), and Super AI (ASI), and by operational functionality into Reactive Machines, Limited Memory, Theory of Mind, and Self-Aware systems.",
                "intuition": "Like the difference between a master chess engine that can ONLY play chess (Narrow AI) versus a human child who can learn chess, paint a picture, speak languages, and ride a bicycle (General AI).",
                "example": "Classification Matrix:\n1. ANI (Artificial Narrow AI): Solves one domain exceptionally (AlphaGo, Siri, facial recognition, autonomous driving)\n2. AGI (Artificial General Intelligence): Hypothetical system with human-level reasoning, abstraction, and adaptability across any intellectual task\n3. ASI (Artificial Superintelligence): Hypothetical intelligence far surpassing the smartest human minds across all creative, scientific, and social fields",
                "key_points": [
                    "All AI in existence today is Artificial Narrow AI (ANI)",
                    "Reactive Machines have no memory and react only to current inputs (e.g., IBM Deep Blue)",
                    "Limited Memory systems use historical data to guide current actions (e.g., Self-driving cars, LLMs)",
                    "AGI and ASI remain active frontiers of theoretical research and alignment safety"
                ],
                "practice": "Is a self-driving Tesla car an example of Narrow AI (ANI) or General AI (AGI)? Why?",
                "common_mistakes": [
                    "Assuming today's LLMs are AGI because they can answer diverse questions (they are still ANI without autonomous causal reasoning)",
                    "Overlooking alignment and safety when scaling to AGI"
                ]
            },
            "generative_ai": {
                "title": "Generative AI & LLMs",
                "what": "Generative AI is a modern subfield of Deep Learning that uses foundation models and Transformers to generate new, original content — including text, code, audio, and images — from user prompts.",
                "intuition": "Traditional AI is like an art judge (discriminative — classifies if an image is a cat or dog). Generative AI is like the artist (creates a photorealistic picture of a cat playing piano).",
                "example": "```python\n# Conceptual Generative Pipeline\nprompt = 'Explain quantum computing in simple terms'\nresponse = llm.generate(\n    prompt=prompt,\n    temperature=0.7,\n    max_tokens=250\n)\nprint(response.text)\n```",
                "key_points": [
                    "Transformer Architecture: Uses self-attention mechanisms to weigh relationships between tokens across long contexts",
                    "Foundation Models: Pre-trained on vast internet-scale datasets, then fine-tuned for instruction following (RLHF)",
                    "Multimodal Capabilities: Processes and cross-synthesizes text, code, vision, audio, and video",
                    "RAG (Retrieval-Augmented Generation): Grounds generation in verified external documents to prevent hallucinations"
                ],
                "practice": "What is the role of the 'temperature' parameter in generative LLMs, and when should it be set close to 0?",
                "common_mistakes": [
                    "Treating Generative AI as a search database rather than a probabilistic reasoning engine",
                    "Neglecting prompt grounding and verification (leading to unchecked hallucinations)"
                ]
            }
        }
    },
    "machine_learning": {
        "keywords": ["machine learning", "ml", "neural network", "deep learning", "model", "training", "prediction", "classification", "regression", "clustering"],
        "topics": {
            "basics": {
                "title": "Machine Learning Basics",
                "what": "Machine Learning is a subset of AI where systems learn patterns from data to make predictions without being explicitly programmed.",
                "intuition": "Instead of writing rules like 'if temperature > 30, turn on AC', ML learns the pattern from thousands of examples.",
                "example": "ML types:\n- Supervised: Learn from labeled examples (spam detection)\n- Unsupervised: Find hidden patterns (customer segments)\n- Reinforcement: Learn through rewards (game AI)",
                "key_points": ["Data is the fuel", "Features = input variables", "Labels = target variable", "Training = learning from data", "Testing = evaluating on new data"],
                "practice": "Name 3 real-world applications of supervised learning.",
                "common_mistakes": ["Using ML when simple rules work", "Not enough training data", "Overfitting to training data"]
            },
            "regression": {
                "title": "Linear Regression",
                "what": "Linear Regression finds the best straight line (or hyperplane) that predicts a continuous output from input features.",
                "intuition": "Imagine plotting student study hours vs exam scores. Linear regression finds the line that best fits all the dots.",
                "example": "```python\nfrom sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\npredictions = model.predict(X_test)\n```",
                "key_points": ["y = mx + b (simple case)", "Minimizes squared errors", "Good baseline model", "Assumes linear relationship"],
                "practice": "If the line is y = 2x + 5, what's the predicted y when x = 10?",
                "common_mistakes": ["Assuming causation from correlation", "Not checking assumptions", "Using for categorical outcomes"]
            },
            "classification": {
                "title": "Classification",
                "what": "Classification predicts a categorical label (class) for a given input. Examples: spam/not spam, pass/fail.",
                "intuition": "Classification is like sorting mail into categories. The model learns what each category looks like from examples.",
                "example": "```python\nfrom sklearn.tree import DecisionTreeClassifier\nmodel = DecisionTreeClassifier()\nmodel.fit(X_train, y_train)\naccuracy = model.score(X_test, y_test)\n```",
                "key_points": ["Output is a category", "Common algorithms: Logistic Regression, Decision Trees, SVM, Random Forest", "Evaluated by accuracy, precision, recall, F1-score"],
                "practice": "When would you use precision over accuracy? Give an example.",
                "common_mistakes": ["Class imbalance issues", "Not separating train/test sets", "Confusing precision and recall"]
            },
            "decision_trees": {
                "title": "Decision Trees",
                "what": "Decision trees split data into branches based on feature values, like a flowchart of if-else decisions.",
                "intuition": "Like 20 questions: each question narrows down the possibilities until you reach an answer.",
                "example": "```python\nfrom sklearn.tree import DecisionTreeClassifier\ntree = DecisionTreeClassifier(max_depth=5)\ntree.fit(X_train, y_train)\n# Visualize with plot_tree(tree)\n```",
                "key_points": ["Easy to interpret", "No feature scaling needed", "Prone to overfitting", "Fixed by pruning or using Random Forests"],
                "practice": "Draw a decision tree for deciding 'Should I study today?' with 3 features.",
                "common_mistakes": ["Overfitting with unlimited depth", "Not pruning", "Sensitive to data changes"]
            },
            "neural_networks": {
                "title": "Neural Networks",
                "what": "Neural networks are computing systems inspired by the human brain, made of interconnected layers of nodes (neurons).",
                "intuition": "Like a committee making a decision. Each layer extracts more complex features until the final layer makes the prediction.",
                "example": "```python\nfrom sklearn.neural_network import MLPClassifier\nmodel = MLPClassifier(hidden_layer_sizes=(100, 50))\nmodel.fit(X_train, y_train)\n```",
                "key_points": ["Input, hidden, and output layers", "Activation functions (ReLU, Sigmoid)", "Learns via backpropagation", "Requires lots of data"],
                "practice": "Name one activation function used in Neural Networks.",
                "common_mistakes": ["Not scaling inputs", "Too many layers causing vanishing gradients", "Overfitting on small datasets"]
            },
            "overfitting": {
                "title": "Overfitting Solutions",
                "what": "Overfitting happens when a model learns the training data too well, failing to generalize. Solutions include regularization and cross-validation.",
                "intuition": "Like memorizing the answers to a practice test but failing the real exam because the questions changed slightly.",
                "example": "```python\nfrom sklearn.linear_model import Ridge\n# Ridge regression applies L2 regularization\nmodel = Ridge(alpha=1.0)\nmodel.fit(X_train, y_train)\n```",
                "key_points": ["Regularization (L1/L2)", "Cross-validation", "Early stopping", "Getting more data"],
                "practice": "Explain why early stopping helps prevent overfitting.",
                "common_mistakes": ["Using testing data during training", "Ignoring validation loss", "Training for too many epochs"]
            },
            "model_evaluation": {
                "title": "Model Evaluation",
                "what": "Model evaluation assesses how well a model performs using metrics like accuracy, precision, recall, F1, and confusion matrix.",
                "intuition": "Like grading a test. Accuracy is overall correct, but precision/recall tell you what specific types of mistakes were made.",
                "example": "```python\nfrom sklearn.metrics import classification_report, confusion_matrix\nprint(confusion_matrix(y_test, y_pred))\nprint(classification_report(y_test, y_pred))\n```",
                "key_points": ["Accuracy isn't always best for imbalanced data", "Precision: false positives matter", "Recall: false negatives matter", "ROC-AUC evaluates trade-offs"],
                "practice": "If identifying cancer, is recall or precision more important?",
                "common_mistakes": ["Relying only on accuracy for imbalanced classes", "Testing on training data", "Confusing precision and recall"]
            }
        }
    },
    "web_development": {
        "keywords": ["web", "html", "css", "javascript", "react", "frontend", "backend", "website", "component", "state", "props", "hook", "api", "rest"],
        "topics": {
            "html_basics": {
                "title": "HTML Fundamentals",
                "what": "HTML (HyperText Markup Language) is the standard language for creating web pages. It defines the structure of content.",
                "intuition": "HTML is the skeleton of a webpage. CSS is the skin and clothes. JavaScript is the brain and muscles.",
                "example": "```html\n<!DOCTYPE html>\n<html>\n<head>\n  <title>Capacity Connect</title>\n</head>\n<body>\n  <h1>Welcome to Learning</h1>\n  <p>Start your journey today.</p>\n</body>\n</html>\n```",
                "key_points": ["Uses tags like <h1>, <p>, <div>", "Nested structure", "Semantic tags (header, nav, main)", "Forms for user input"],
                "practice": "Create an HTML page with a heading, paragraph, and an image.",
                "common_mistakes": ["Missing closing tags", "Using div for everything instead of semantic tags", "Not including alt text on images"]
            },
            "react_components": {
                "title": "React Components",
                "what": "React components are reusable UI building blocks. Each component returns JSX (HTML-like syntax) describing what should appear on screen.",
                "intuition": "Think of components as LEGO bricks. Each brick has its own shape and color, and you snap them together to build bigger structures.",
                "example": "```jsx\nfunction CourseCard({ title, instructor }) {\n  return (\n    <div className=\"card\">\n      <h2>{title}</h2>\n      <p>By {instructor}</p>\n    </div>\n  );\n}\n```",
                "key_points": ["Function components (modern approach)", "Receive props as arguments", "Return JSX", "Can be composed together"],
                "practice": "Create a 'QuizQuestion' component that shows a question and 4 options.",
                "common_mistakes": ["Mutating props directly", "Missing key prop in lists", "Too much logic inside components"]
            },
            "react_state": {
                "title": "React State & Hooks",
                "what": "State manages dynamic data in React. useState is the most common hook for adding state to functional components.",
                "intuition": "State is like the component's memory. When state changes, React re-renders the UI to reflect the new data.",
                "example": "```jsx\nimport { useState } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n  return (\n    <button onClick={() => setCount(count + 1)}>\n      Clicked {count} times\n    </button>\n  );\n}\n```",
                "key_points": ["useState returns [value, setter]", "State updates trigger re-renders", "Use useEffect for side effects", "State should be immutable"],
                "practice": "Build a simple todo list with add and remove functionality using useState.",
                "common_mistakes": ["Directly mutating state", "Using state for everything (use props when possible)", "Forgetting dependency array in useEffect"]
            },
            "css_layout": {
                "title": "CSS Layout",
                "what": "CSS layout defines how elements are positioned. Flexbox is for 1D layouts, Grid is for 2D layouts.",
                "intuition": "Flexbox is like arranging items in a single row or column. Grid is like laying out items on a chessboard.",
                "example": "```css\n.container {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n}\n```",
                "key_points": ["Flexbox: display: flex", "Grid: display: grid", "Responsive design", "Media queries"],
                "practice": "Create a flex container that centers its children horizontally and vertically.",
                "common_mistakes": ["Confusing align-items and justify-content", "Using floats for layout", "Forgetting display: flex on the parent container"]
            },
            "api_design": {
                "title": "API Design",
                "what": "REST API design principles define how to create standard, predictable web interfaces.",
                "intuition": "Like a menu in a restaurant. The API defines what you can ask for (endpoints) and what you'll get back (JSON).",
                "example": "```\nGET /api/users - Get all users\nPOST /api/users - Create a user\nGET /api/users/123 - Get user 123\nDELETE /api/users/123 - Delete user 123\n```",
                "key_points": ["Use HTTP methods correctly (GET, POST, PUT, DELETE)", "Stateless interactions", "Standard HTTP status codes", "JSON formats"],
                "practice": "What HTTP method would you use to update a user's profile?",
                "common_mistakes": ["Using GET for state-changing operations", "Returning 200 OK for errors", "Inconsistent URL naming"]
            }
        }
    },
    "cloud_computing": {
        "keywords": ["cloud", "aws", "azure", "docker", "kubernetes", "deploy", "server", "hosting", "ec2", "s3", "lambda"],
        "topics": {
            "aws_basics": {
                "title": "AWS Core Services",
                "what": "Amazon Web Services provides on-demand cloud computing. Key services: EC2 (compute), S3 (storage), IAM (security).",
                "intuition": "AWS is like renting computers, storage, and tools over the internet instead of buying and maintaining your own hardware.",
                "example": "Key services:\n- EC2: Virtual servers\n- S3: Object storage (like a hard drive in the cloud)\n- IAM: Identity and access management\n- Lambda: Run code without servers",
                "key_points": ["Pay-as-you-go pricing", "Global infrastructure", "Scalable on demand", "IAM controls who can access what"],
                "practice": "Explain the difference between EC2 and Lambda in your own words.",
                "common_mistakes": ["Not setting up proper IAM permissions", "Leaving instances running (cost)", "Not using security groups"]
            },
            "docker": {
                "title": "Docker Containers",
                "what": "Docker packages applications and dependencies into standardized units called containers.",
                "intuition": "Like shipping containers. Instead of custom loading each item onto a ship, everything goes in a standard box that fits anywhere.",
                "example": "```dockerfile\nFROM python:3.9\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD [\"python\", \"app.py\"]\n```",
                "key_points": ["Images are blueprints", "Containers are running instances", "Dockerfile defines the image", "docker-compose manages multi-container apps"],
                "practice": "Write a command to build a Docker image from a Dockerfile.",
                "common_mistakes": ["Including secrets in Dockerfile", "Images being too large", "Running containers as root user"]
            },
            "serverless": {
                "title": "Serverless Computing",
                "what": "Serverless allows you to build and run applications without thinking about servers. Code runs in response to events.",
                "intuition": "Like taking a taxi instead of owning a car. You only pay for the exact time you are using the service, and maintenance is handled for you.",
                "example": "```python\n# AWS Lambda Example\ndef lambda_handler(event, context):\n    name = event.get('name', 'World')\n    return {'statusCode': 200, 'body': f'Hello, {name}!'}\n```",
                "key_points": ["Event-driven architecture", "Zero server maintenance", "Auto-scaling", "Pay only for execution time"],
                "practice": "Name one advantage of serverless over traditional EC2 instances.",
                "common_mistakes": ["Cold starts affecting performance", "Building monolithic functions", "Poor cost monitoring leading to surprise bills"]
            }
        }
    },
    "cybersecurity": {
        "keywords": ["security", "cyber", "hacking", "firewall", "encryption", "password", "vulnerability", "attack", "penetration", "network security"],
        "topics": {
            "network_security": {
                "title": "Network Security Basics",
                "what": "Network security involves protecting data in transit across networks using firewalls, encryption, and monitoring.",
                "intuition": "Like having locks, alarms, and security guards for your data's journey across the internet.",
                "example": "Key concepts:\n- Firewall: Filters traffic\n- VPN: Encrypted tunnel\n- SSL/TLS: Encrypts web traffic\n- IDS/IPS: Detects attacks",
                "key_points": ["Defense in depth (layered security)", "Least privilege principle", "Encryption at rest and in transit", "Regular security audits"],
                "practice": "What's the difference between IDS and IPS?",
                "common_mistakes": ["Using default passwords", "Not updating software", "Ignoring security logs"]
            },
            "owasp": {
                "title": "OWASP Top 10",
                "what": "The OWASP Top 10 is a standard awareness document representing the most critical security risks to web applications.",
                "intuition": "It's the 'most wanted' list of web vulnerabilities. If you secure these, you prevent the majority of attacks.",
                "example": "Common risks:\n- Injection (SQLi)\n- Broken Authentication\n- Sensitive Data Exposure\n- XSS (Cross-Site Scripting)",
                "key_points": ["SQL Injection: Use parameterized queries", "XSS: Escape user input", "Keep dependencies updated", "Implement strict access controls"],
                "practice": "How do you prevent SQL Injection?",
                "common_mistakes": ["Trusting user input", "Rolling your own crypto", "Hardcoding secrets in source code"]
            },
            "cryptography": {
                "title": "Cryptography Basics",
                "what": "Cryptography is the practice of securing communication from adversaries. Includes symmetric/asymmetric encryption and hashing.",
                "intuition": "Like a secret code ring. Symmetric uses one key to lock/unlock. Asymmetric uses a public key to lock and a private key to unlock.",
                "example": "```python\nimport hashlib\n# Hashing a password\nh = hashlib.sha256()\nh.update(b'my_password')\nprint(h.hexdigest())\n```",
                "key_points": ["Symmetric: AES (same key)", "Asymmetric: RSA (public/private pair)", "Hashing: SHA-256 (one-way)", "Salting prevents rainbow table attacks"],
                "practice": "What is the main difference between hashing and encryption?",
                "common_mistakes": ["Using weak hashing like MD5", "Not using a salt for passwords", "Storing encryption keys insecurely"]
            }
        }
    }
}

GREETINGS = ["hello", "hi", "hey", "good morning", "good evening", "good afternoon", "namaste"]
FRUSTRATION_KEYWORDS = ["confused", "don't understand", "not getting", "help me", "stuck", "difficult", "hard", "complicated", "unclear"]
ADVANCED_KEYWORDS = ["deep dive", "advanced", "go deeper", "explain completely", "in detail", "comprehensive", "thorough"]
BEGINNER_KEYWORDS = ["beginner", "basics", "simple", "easy", "introduction", "start from scratch", "new to", "first time"]


def get_user_context(user_id=None, custom_name=None):
    conn = get_db()
    user = None
    if user_id and str(user_id).isdigit() and int(user_id) > 0:
        user = conn.execute("SELECT * FROM users WHERE id=?", (int(user_id),)).fetchone()

    # If not found by user_id but custom_name provided, search by username or full_name
    if not user and custom_name:
        clean_name = custom_name.strip()
        user = conn.execute("SELECT * FROM users WHERE username LIKE ? OR full_name LIKE ?", 
                            (clean_name, f"%{clean_name}%")).fetchone()
        if user:
            user_id = user["id"]

    if not user:
        conn.close()
        if custom_name and custom_name.strip():
            clean = custom_name.strip()
            return {
                "user": {
                    "id": 0,
                    "username": clean.lower().replace(" ", "_"),
                    "full_name": clean,
                    "role": "trainee",
                    "department": "Digital Capacity Building"
                },
                "enrollments": [],
                "quiz_scores": [],
                "recent_lessons": [],
                "weak_areas": [],
                "projects": []
            }
        return None

    # User found in DB
    user_dict = dict(user)
    if custom_name and custom_name.strip():
        user_dict["full_name"] = custom_name.strip()

    enrollments = conn.execute("""
        SELECT e.*, c.title, c.category, c.difficulty
        FROM enrollments e JOIN courses c ON e.course_id = c.id
        WHERE e.user_id=?
    """, (user_id,)).fetchall()

    quiz_scores = conn.execute("""
        SELECT q.title, qa.score
        FROM quiz_attempts qa JOIN quizzes q ON qa.quiz_id = q.id
        WHERE qa.user_id=?
        ORDER BY qa.rowid DESC LIMIT 5
    """, (user_id,)).fetchall()

    recent_lessons = conn.execute("""
        SELECT l.title, m.title as module_title, c.title as course_title
        FROM lesson_progress lp
        JOIN lessons l ON lp.lesson_id = l.id
        JOIN modules m ON l.module_id = m.id
        JOIN courses c ON m.course_id = c.id
        WHERE lp.user_id=? AND lp.completed=1
        LIMIT 5
    """, (user_id,)).fetchall()

    weak_areas = conn.execute("""
        SELECT q.title, qa.score
        FROM quiz_attempts qa JOIN quizzes q ON qa.quiz_id = q.id
        WHERE qa.user_id=? AND qa.score < 60
    """, (user_id,)).fetchall()

    projects = conn.execute("""
        SELECT p.title, p.status, p.grade, p.trainer_feedback, c.title as course_title
        FROM projects p JOIN courses c ON p.course_id = c.id
        WHERE p.user_id=?
    """, (user_id,)).fetchall()

    conn.close()
    return {
        "user": user_dict,
        "enrollments": [dict(e) for e in enrollments],
        "quiz_scores": [dict(q) for q in quiz_scores],
        "recent_lessons": [dict(l) for l in recent_lessons],
        "weak_areas": [dict(w) for w in weak_areas],
        "projects": [dict(p) for p in projects]
    }


def detect_intent(message):
    msg = message.lower().strip()
    words = set(msg.split())

    single_greetings = {"hello", "hi", "hey", "namaste"}
    if words & single_greetings:
        return "greeting"
    if any(phrase in msg for phrase in ["good morning", "good evening", "good afternoon"]):
        return "greeting"

    if any(phrase in msg for phrase in ["quiz me", "quiz", "test me", "assessment", "practice question", "ask me a question"]):
        return "quiz"

    if any(phrase in msg for phrase in ["what should i learn", "recommend", "what course", "next lesson", "what next", "suggest"]):
        return "recommendation"

    if any(phrase in msg for phrase in ["my course", "enrolled", "my progress", "dashboard", "what am i learning"]):
        return "progress"

    if any(phrase in msg for phrase in ["notes", "make notes", "create notes", "summarize", "revision"]):
        return "notes"

    if any(phrase in msg for phrase in ["project", "submission", "feedback", "grade"]):
        return "project"

    if any(phrase in msg for phrase in ["certificate", "cert", "completion", "completed"]):
        return "certificate"

    if any(phrase in msg for phrase in ["announcement", "news", "update", "notice"]):
        return "announcement"

    if any(phrase in msg for phrase in ["navigate", "go to", "open", "take me to", "show me"]):
        return "navigation"

    t_match, _ = find_best_topic(msg)
    if t_match:
        return "teach"

    for topic_key, topic_data in TOPIC_KNOWLEDGE.items():
        if any(re.search(r'\b' + re.escape(kw) + r'(?:s|es)?\b', msg) for kw in topic_data["keywords"]):
            return "teach"

    if "?" in msg:
        return "question"

    return "general"


def detect_skill_level(message):
    msg = message.lower()
    if any(w in msg for w in ADVANCED_KEYWORDS):
        return "advanced"
    if any(w in msg for w in BEGINNER_KEYWORDS):
        return "beginner"
    return "intermediate"


def detect_frustration(message):
    return any(w in message.lower() for w in FRUSTRATION_KEYWORDS)


TOPIC_ALIASES = {
    # Variables
    "variable": ("python", "variables"),
    "variables": ("python", "variables"),
    "var": ("python", "variables"),
    "vars": ("python", "variables"),
    "variable assignment": ("python", "variables"),
    "python variable": ("python", "variables"),
    "python variables": ("python", "variables"),

    # Functions
    "function": ("python", "functions"),
    "functions": ("python", "functions"),
    "def": ("python", "functions"),
    "method": ("python", "functions"),
    "methods": ("python", "functions"),
    "parameter": ("python", "functions"),
    "parameters": ("python", "functions"),
    "argument": ("python", "functions"),
    "arguments": ("python", "functions"),
    "return value": ("python", "functions"),
    "python function": ("python", "functions"),
    "python functions": ("python", "functions"),

    # Loops
    "loop": ("python", "loops"),
    "loops": ("python", "loops"),
    "for loop": ("python", "loops"),
    "for loops": ("python", "loops"),
    "while loop": ("python", "loops"),
    "while loops": ("python", "loops"),
    "iteration": ("python", "loops"),
    "iterations": ("python", "loops"),
    "iterate": ("python", "loops"),

    # Data Types
    "data type": ("python", "data_types"),
    "data types": ("python", "data_types"),
    "datatype": ("python", "data_types"),
    "datatypes": ("python", "data_types"),
    "list": ("python", "data_types"),
    "lists": ("python", "data_types"),
    "dictionary": ("python", "data_types"),
    "dictionaries": ("python", "data_types"),
    "dict": ("python", "data_types"),
    "tuple": ("python", "data_types"),
    "tuples": ("python", "data_types"),
    "string": ("python", "data_types"),
    "strings": ("python", "data_types"),
    "str": ("python", "data_types"),
    "int": ("python", "data_types"),
    "integer": ("python", "data_types"),
    "boolean": ("python", "data_types"),
    "bool": ("python", "data_types"),
    "float": ("python", "data_types"),

    # OOP
    "oop": ("python", "oop"),
    "object oriented": ("python", "oop"),
    "object oriented programming": ("python", "oop"),
    "class": ("python", "oop"),
    "classes": ("python", "oop"),
    "object": ("python", "oop"),
    "objects": ("python", "oop"),
    "inheritance": ("python", "oop"),
    "encapsulation": ("python", "oop"),
    "polymorphism": ("python", "oop"),

    # File Handling
    "file": ("python", "file_handling"),
    "files": ("python", "file_handling"),
    "file handling": ("python", "file_handling"),
    "open file": ("python", "file_handling"),
    "read file": ("python", "file_handling"),
    "write file": ("python", "file_handling"),
    "file io": ("python", "file_handling"),

    # Error Handling
    "error": ("python", "error_handling"),
    "errors": ("python", "error_handling"),
    "exception": ("python", "error_handling"),
    "exceptions": ("python", "error_handling"),
    "try except": ("python", "error_handling"),
    "error handling": ("python", "error_handling"),

    # Artificial Intelligence
    "artificial intelligence": ("artificial_intelligence", "basics"),
    "artificial intelligence basics": ("artificial_intelligence", "basics"),
    "ai": ("artificial_intelligence", "basics"),
    "ai basics": ("artificial_intelligence", "basics"),
    "what is ai": ("artificial_intelligence", "basics"),
    "what is artificial intelligence": ("artificial_intelligence", "basics"),
    "tell me about artificial intelligence": ("artificial_intelligence", "basics"),
    "tell me about ai": ("artificial_intelligence", "basics"),
    "types of ai": ("artificial_intelligence", "types"),
    "narrow ai": ("artificial_intelligence", "types"),
    "ani": ("artificial_intelligence", "types"),
    "general ai": ("artificial_intelligence", "types"),
    "agi": ("artificial_intelligence", "types"),
    "super ai": ("artificial_intelligence", "types"),
    "asi": ("artificial_intelligence", "types"),
    "generative ai": ("artificial_intelligence", "generative_ai"),
    "genai": ("artificial_intelligence", "generative_ai"),
    "llm": ("artificial_intelligence", "generative_ai"),
    "llms": ("artificial_intelligence", "generative_ai"),
    "large language model": ("artificial_intelligence", "generative_ai"),
    "large language models": ("artificial_intelligence", "generative_ai"),

    # Machine Learning
    "machine learning": ("machine_learning", "basics"),
    "ml": ("machine_learning", "basics"),
    "linear regression": ("machine_learning", "regression"),
    "regression": ("machine_learning", "regression"),
    "regressions": ("machine_learning", "regression"),
    "classification": ("machine_learning", "classification"),
    "classifications": ("machine_learning", "classification"),
    "classifier": ("machine_learning", "classification"),
    "decision tree": ("machine_learning", "decision_trees"),
    "decision trees": ("machine_learning", "decision_trees"),
    "random forest": ("machine_learning", "decision_trees"),
    "neural network": ("machine_learning", "neural_networks"),
    "neural networks": ("machine_learning", "neural_networks"),
    "deep learning": ("machine_learning", "neural_networks"),
    "cnn": ("machine_learning", "neural_networks"),
    "rnn": ("machine_learning", "neural_networks"),
    "overfitting": ("machine_learning", "overfitting"),
    "underfitting": ("machine_learning", "overfitting"),
    "regularization": ("machine_learning", "overfitting"),
    "cross validation": ("machine_learning", "overfitting"),
    "model evaluation": ("machine_learning", "model_evaluation"),
    "accuracy": ("machine_learning", "model_evaluation"),
    "precision": ("machine_learning", "model_evaluation"),
    "recall": ("machine_learning", "model_evaluation"),
    "f1 score": ("machine_learning", "model_evaluation"),
    "confusion matrix": ("machine_learning", "model_evaluation"),

    # Web Dev
    "html": ("web_development", "html_basics"),
    "html5": ("web_development", "html_basics"),
    "html basics": ("web_development", "html_basics"),
    "react": ("web_development", "react_components"),
    "react component": ("web_development", "react_components"),
    "react components": ("web_development", "react_components"),
    "component": ("web_development", "react_components"),
    "components": ("web_development", "react_components"),
    "jsx": ("web_development", "react_components"),
    "props": ("web_development", "react_components"),
    "react state": ("web_development", "react_state"),
    "state": ("web_development", "react_state"),
    "usestate": ("web_development", "react_state"),
    "useeffect": ("web_development", "react_state"),
    "hooks": ("web_development", "react_state"),
    "react hooks": ("web_development", "react_state"),
    "css": ("web_development", "css_layout"),
    "css layout": ("web_development", "css_layout"),
    "flexbox": ("web_development", "css_layout"),
    "grid": ("web_development", "css_layout"),
    "api": ("web_development", "api_design"),
    "apis": ("web_development", "api_design"),
    "rest": ("web_development", "api_design"),
    "rest api": ("web_development", "api_design"),
    "api design": ("web_development", "api_design"),

    # Cloud Computing
    "aws": ("cloud_computing", "aws_basics"),
    "ec2": ("cloud_computing", "aws_basics"),
    "s3": ("cloud_computing", "aws_basics"),
    "iam": ("cloud_computing", "aws_basics"),
    "lambda": ("cloud_computing", "aws_basics"),
    "cloud": ("cloud_computing", "aws_basics"),
    "cloud computing": ("cloud_computing", "aws_basics"),
    "docker": ("cloud_computing", "docker"),
    "container": ("cloud_computing", "docker"),
    "containers": ("cloud_computing", "docker"),
    "dockerfile": ("cloud_computing", "docker"),
    "kubernetes": ("cloud_computing", "docker"),
    "k8s": ("cloud_computing", "docker"),
    "serverless": ("cloud_computing", "serverless"),
    "serverless computing": ("cloud_computing", "serverless"),

    # Cybersecurity
    "security": ("cybersecurity", "network_security"),
    "cybersecurity": ("cybersecurity", "network_security"),
    "network security": ("cybersecurity", "network_security"),
    "firewall": ("cybersecurity", "network_security"),
    "firewalls": ("cybersecurity", "network_security"),
    "vpn": ("cybersecurity", "network_security"),
    "owasp": ("cybersecurity", "owasp"),
    "sql injection": ("cybersecurity", "owasp"),
    "sqli": ("cybersecurity", "owasp"),
    "xss": ("cybersecurity", "owasp"),
    "cryptography": ("cybersecurity", "cryptography"),
    "crypto": ("cybersecurity", "cryptography"),
    "encryption": ("cybersecurity", "cryptography"),
    "decryption": ("cybersecurity", "cryptography"),
}


def find_best_topic(message):
    if not message:
        return None, None
    msg = message.lower().strip()

    # 1. Check direct aliases (sort by length descending so longer phrases match first)
    for alias, pair in sorted(TOPIC_ALIASES.items(), key=lambda x: len(x[0]), reverse=True):
        if re.search(r'\b' + re.escape(alias) + r'\b', msg):
            return pair

    # 2. Check subtopic keys and titles across TOPIC_KNOWLEDGE
    best_match = None
    best_sub = None
    best_score = 0

    for topic_key, topic_data in TOPIC_KNOWLEDGE.items():
        for sub_key, sub_data in topic_data["topics"].items():
            key_clean = sub_key.replace('_', ' ')
            title_clean = sub_data["title"].lower()
            
            sub_score = 0
            if re.search(r'\b' + re.escape(key_clean) + r'(?:s|es)?\b', msg):
                sub_score += 3
            if re.search(r'\b' + re.escape(title_clean) + r'\b', msg):
                sub_score += 4
            for part in sub_key.split('_'):
                if len(part) > 2 and re.search(r'\b' + re.escape(part) + r'(?:s|es)?\b', msg):
                    sub_score += 1
            if sub_score > best_score:
                best_score = sub_score
                best_match = topic_key
                best_sub = sub_key

    if best_match and best_sub:
        return best_match, best_sub

    # 3. Keyword matching across topics
    for topic_key, topic_data in TOPIC_KNOWLEDGE.items():
        score = 0
        for kw in topic_data["keywords"]:
            if re.search(r'\b' + re.escape(kw) + r'(?:s|es)?\b', msg):
                score += 1
        if score > best_score:
            best_score = score
            best_match = topic_key

    if best_match:
        first_key = list(TOPIC_KNOWLEDGE[best_match]["topics"].keys())[0]
        return best_match, first_key

    return None, None


def teach_topic(topic_key, subtopic_key, skill_level="beginner", is_frustrated=False):
    topic_data = TOPIC_KNOWLEDGE.get(topic_key)
    if not topic_data:
        return None

    subtopic = topic_data["topics"].get(subtopic_key)
    if not subtopic:
        subtopic = list(topic_data["topics"].values())[0]

    out = [
        f"✦ {subtopic['title']} — Easy Learning Guide\n",
        f"◈ Concept Overview:\n{subtopic['what']}\n",
        f"❯ Intuition & Everyday Analogy:\n{subtopic['intuition']}\n",
        f"❖ Code Example & How It Works:\n{subtopic['example']}\n",
        "📌 Key Rules to Remember:\n" + "\n".join(f"• {p}" for p in subtopic["key_points"]) + "\n"
    ]

    if subtopic.get("common_mistakes"):
        out.append("⚠️ Common Mistakes to Avoid:\n" + "\n".join(f"• {m}" for m in subtopic["common_mistakes"]) + "\n")

    out.append(f"🎯 Quick Practice Challenge:\n{subtopic['practice']}\n")
    out.append("💡 Select 'Quiz' to test your understanding, 'Study Notes' for printable PDF notes, or 'Study Visuals' for diagrams!")
    return "\n".join(out)


def handle_greeting(context, message="", custom_name=None):
    name = "Learner"
    if custom_name and custom_name.strip():
        name = custom_name.strip().split()[0]
    elif context and context.get("user") and context["user"].get("full_name"):
        name = context["user"]["full_name"].split()[0]

    # Dynamically extract user name if introduced in the message (e.g. "hi i am Sneha", "my name is Alex")
    if message:
        import re
        m = re.search(r'(?:i am|i\'m|my name is|this is|call me)\s+([a-zA-Z]+)', message, re.IGNORECASE)
        if m:
            extracted = m.group(1).capitalize()
            if extracted.lower() not in ("sastra", "astra"):
                name = extracted

    enrollments = context["enrollments"] if context else []
    quiz_scores = context["quiz_scores"] if context else []

    greeting_lead = f"Hello {name}!" if name and name.lower() not in ("learner", "user", "guest") else "Hello!"
    response = f"{greeting_lead} I'm Sastra, your AI Learning Assistant for Capacity Connect.\n\n"

    if enrollments:
        courses = [e["title"] for e in enrollments[:3]]
        response += f"You're currently enrolled in: {', '.join(courses)}.\n"
        if quiz_scores:
            latest = quiz_scores[0]
            if latest["score"] >= 60:
                response += f"Great job on your last quiz ({latest['title']}) — you scored {latest['score']}%! 🎯\n"
            else:
                response += f"I see you scored {latest['score']}% on {latest['title']}. Want me to help you review that topic? 💡\n"
        response += "\nHow can I help you today? I can:\n"
        response += "❯ 📖 Teach a concept\n❯ 🎯 Quiz you on any topic\n❯ 🧭 Recommend what to learn next\n❯ 📊 Check your progress\n❯ 📄 Help with projects or PDF notes"
    else:
        response += "I'm here to help you learn, practice, and grow. What would you like to work on today?"

    return response


def handle_progress(context):
    if not context:
        return "I don't have your learning data yet. Please make sure you're logged in so I can track your progress."

    enrollments = context["enrollments"]
    quiz_scores = context["quiz_scores"]
    projects = context["projects"]

    response = "**Your Learning Progress**\n\n"

    if enrollments:
        response += "**Enrolled Courses:**\n"
        for e in enrollments:
            status = "Completed" if e["completed"] else f"{e['progress_pct']}% complete"
            emoji = "green" if e["completed"] else "blue"
            response += f"- **{e['title']}** ({e['category']}) — {status}\n"
        response += "\n"
    else:
        response += "You're not enrolled in any courses yet. Let me recommend some!\n\n"

    if quiz_scores:
        response += "**Recent Quiz Scores:**\n"
        for q in quiz_scores:
            score_emoji = "excellent" if q["score"] >= 80 else "good" if q["score"] >= 60 else "needs review"
            response += f"- {q['title']}: **{q['score']}%** ({score_emoji})\n"
        response += "\n"

    if projects:
        response += "**Projects:**\n"
        for p in projects:
            response += f"- {p['title']} — Status: **{p['status']}**"
            if p["grade"]:
                response += f" | Grade: **{p['grade']}**"
            if p["trainer_feedback"]:
                response += f"\n  Feedback: _{p['trainer_feedback']}_"
            response += "\n"

    if context["weak_areas"]:
        response += "\n**Areas to Review:**\n"
        for w in context["weak_areas"]:
            response += f"- {w['title']} (scored {w['score']}%)\n"
        response += "\nWant me to help you review any of these?"

    return response


def handle_recommendation(context):
    if not context:
        return "I need to know your learning history to make recommendations. What topics interest you?"

    enrollments = context["enrollments"]
    weak_areas = context["weak_areas"]
    quiz_scores = context["quiz_scores"]

    response = "**Personalized Recommendations**\n\n"

    if weak_areas:
        response += "**Priority — Review These:**\n"
        for w in weak_areas[:2]:
            response += f"- **{w['title']}** (you scored {w['score']}%) — Reviewing this will strengthen your foundation.\n"
        response += "\n"

    enrolled_ids = set(e["course_id"] for e in enrollments)
    all_courses = get_db().execute("SELECT * FROM courses").fetchall()

    available = [c for c in all_courses if c["id"] not in enrolled_ids]
    if available:
        response += "**Suggested New Courses:**\n"
        for c in available[:3]:
            response += f"- **{c['title']}** ({c['difficulty']}) — {c['description'][:80]}...\n"
        response += "\n"

    if enrollments:
        incomplete = [e for e in enrollments if not e["completed"] and e["progress_pct"] < 100]
        if incomplete:
            response += "**Continue Where You Left Off:**\n"
            for e in incomplete[:2]:
                response += f"- **{e['title']}** — {e['progress_pct']}% complete\n"

    response += "\nWould you like me to start a lesson, give you a quiz, or explain a concept?"
    return response


QUIZ_BANK = {
    1: [
        {"q": "What is the output of: `print(type(42))`?", "opts": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'number'>"], "ans": 0, "exp": "42 is an integer, so Python creates an int object."},
        {"q": "Which keyword defines a function in Python?", "opts": ["func", "function", "def", "define"], "ans": 2, "exp": "'def' is the keyword used to define functions in Python."},
        {"q": "What does `len()` do?", "opts": ["Calculates length", "Converts to list", "Prints output", "Creates loop"], "ans": 0, "exp": "len() returns the number of items in an object."},
        {"q": "Which is immutable in Python?", "opts": ["List", "Dictionary", "Set", "Tuple"], "ans": 3, "exp": "Tuples cannot be modified after creation."},
        {"q": "Correct file extension for Python?", "opts": [".python", ".py", ".pt", ".pyt"], "ans": 1, "exp": "Python files use the .py extension."},
        {"q": "Which of these is used for Object-Oriented Programming?", "opts": ["functions", "classes", "loops", "variables"], "ans": 1, "exp": "Classes are the blueprint for creating objects in OOP."},
        {"q": "How do you open a file for writing?", "opts": ["open('f', 'r')", "open('f', 'w')", "open('f', 'write')", "open('f', 'a')"], "ans": 1, "exp": "The 'w' mode opens a file for writing, truncating it first."},
        {"q": "Which block handles exceptions?", "opts": ["catch", "handle", "except", "error"], "ans": 2, "exp": "The 'except' block in Python catches and handles exceptions."}
    ],
    2: [
        {"q": "What type of learning uses labeled data?", "opts": ["Unsupervised", "Supervised", "Reinforcement", "Semi-supervised"], "ans": 1, "exp": "Supervised learning trains on labeled input-output pairs."},
        {"q": "What is overfitting?", "opts": ["Model too simple", "Model memorizes training data", "Model is fast", "Model uses too little data"], "ans": 1, "exp": "Overfitting means performing well on training data but poorly on new data."},
        {"q": "Which measures classification accuracy?", "opts": ["MSE", "R-squared", "Accuracy Score", "MAE"], "ans": 2, "exp": "Accuracy Score measures proportion of correct predictions."},
        {"q": "What does a Decision Tree do?", "opts": ["Clusters data", "Splits data by feature values", "Averages data", "Generates random data"], "ans": 1, "exp": "Decision trees recursively split data based on feature values."},
        {"q": "What prevents overfitting?", "opts": ["Adding more layers", "Regularization", "Training longer", "Using less data"], "ans": 1, "exp": "Regularization penalizes complex models to prevent overfitting."},
        {"q": "Which metric cares about false positives?", "opts": ["Recall", "Precision", "MSE", "Accuracy"], "ans": 1, "exp": "Precision measures the accuracy of positive predictions."},
        {"q": "What do neural networks use to learn?", "opts": ["Backpropagation", "Decision Trees", "K-Means", "PCA"], "ans": 0, "exp": "Backpropagation updates weights based on the error gradient."}
    ],
    3: [
        {"q": "What is JSX?", "opts": ["A database", "JavaScript XML syntax extension", "A CSS framework", "A testing tool"], "ans": 1, "exp": "JSX lets you write HTML-like syntax in JavaScript for React components."},
        {"q": "Which hook manages state?", "opts": ["useEffect", "useState", "useContext", "useRef"], "ans": 1, "exp": "useState returns a state value and setter function."},
        {"q": "Props in React are:", "opts": ["Mutable", "Read-only", "Global", "Optional"], "ans": 1, "exp": "Props flow from parent to child and are read-only."},
        {"q": "Which CSS layout is best for 1D?", "opts": ["Grid", "Flexbox", "Table", "Float"], "ans": 1, "exp": "Flexbox is designed for one-dimensional layouts (rows or columns)."},
        {"q": "What does REST stand for?", "opts": ["Representational State Transfer", "Real State Transfer", "Remote Server Transfer", "RESTful"], "ans": 0, "exp": "REST stands for Representational State Transfer."},
        {"q": "What HTTP method creates a resource?", "opts": ["GET", "POST", "PUT", "DELETE"], "ans": 1, "exp": "POST is typically used to create new resources in REST APIs."}
    ],
    4: [
        {"q": "Which AWS service provides compute?", "opts": ["S3", "EC2", "RDS", "IAM"], "ans": 1, "exp": "Amazon EC2 provides resizable compute capacity in the cloud."},
        {"q": "What is a Docker image?", "opts": ["Running container", "Blueprint for container", "Cloud instance", "Database"], "ans": 1, "exp": "A Docker image is a read-only template used to build containers."},
        {"q": "Which service is serverless?", "opts": ["EC2", "Lambda", "EBS", "VPC"], "ans": 1, "exp": "AWS Lambda lets you run code without provisioning servers."},
        {"q": "What manages multi-container Docker apps?", "opts": ["Dockerfile", "docker-compose", "git", "npm"], "ans": 1, "exp": "docker-compose is used to define and run multi-container Docker applications."}
    ],
    5: [
        {"q": "What protects data in transit?", "opts": ["Hashing", "Encryption", "Firewalls", "Antivirus"], "ans": 1, "exp": "Encryption (like TLS) secures data while it's transmitted over networks."},
        {"q": "What attack injects malicious queries?", "opts": ["XSS", "CSRF", "SQL Injection", "DDoS"], "ans": 2, "exp": "SQL Injection involves sending malicious SQL statements to a database."},
        {"q": "Which encryption uses two keys?", "opts": ["Symmetric", "Asymmetric", "Hashing", "Encoding"], "ans": 1, "exp": "Asymmetric encryption uses a public key and a private key."},
        {"q": "What is the OWASP Top 10?", "opts": ["Top hackers", "Top security tools", "Top web vulnerabilities", "Top firewalls"], "ans": 2, "exp": "The OWASP Top 10 lists the most critical security risks to web applications."}
    ]
}


def handle_quiz(message, context):
    msg = message.lower()

    if "start" in msg or "quiz me" in msg or "begin" in msg:
        course_id = None
        if context and context["enrollments"]:
            course_id = context["enrollments"][0]["course_id"]

        if course_id and course_id in QUIZ_BANK:
            questions = QUIZ_BANK[course_id]
            q = random.choice(questions)
            opts_text = "\n".join(f"  {i+1}. {opt}" for i, opt in enumerate(q["opts"]))
            return f"**Quiz Time!**\n\n{q['q']}\n\n{opts_text}\n\nReply with the number of your answer (1-{len(q['opts'])})."

        all_q = []
        for qs in QUIZ_BANK.values():
            all_q.extend(qs)
        q = random.choice(all_q)
        opts_text = "\n".join(f"  {i+1}. {opt}" for i, opt in enumerate(q["opts"]))
        return f"**Quiz Time!**\n\n{q['q']}\n\n{opts_text}\n\nReply with the number (1-{len(q['opts'])})."

    if msg.strip().isdigit():
        choice = int(msg.strip()) - 1
        return f"Got your answer! Let me check... _This would be evaluated against the active quiz in a full implementation._\n\nWant another question, or shall we move to a different topic?"

    return "I'll start a quiz for you! Type **'start quiz'** or **'quiz me on Python'** and I'll pick questions from your enrolled courses."


def handle_project(context):
    if not context or not context["projects"]:
        return "You don't have any projects yet. Projects are assigned as part of your courses. Check with your trainer or browse your course modules."

    response = "**Your Projects**\n\n"
    for p in context["projects"]:
        response += f"**{p['title']}** ({p['course_title']})\n"
        response += f"- Status: {p['status']}\n"
        if p["grade"]:
            response += f"- Grade: {p['grade']}\n"
        if p["trainer_feedback"]:
            response += f"- Feedback: _{p['trainer_feedback']}_\n"
        response += "\n"

    response += "Need help improving any project? I can review your approach, suggest improvements, or help you understand the feedback."
    return response


def handle_notes(message, context):
    msg = message.lower()
    if "make notes" in msg or "create notes" in msg or "generate notes" in msg:
        return ("**Note Creation**\n\n"
                "I can help you create structured notes! Tell me:\n"
                "1. Which topic or lesson?\n"
                "2. What depth? (brief summary / detailed notes)\n\n"
                "Example: *'Make detailed notes on Python functions'*\n\n"
                "I'll organize them with definitions, examples, key points, and practice questions.")
    if "summarize" in msg:
        return "I can summarize a topic or your lesson content. Which topic would you like me to summarize?"
    return ("**Notes**\n\n"
            "I can help you:\n"
            "- **Create notes** on any topic\n"
            "- **Summarize** a lesson or concept\n"
            "- **Generate flashcards** for revision\n"
            "- **Convert** your notes into a study guide\n\n"
            "What would you like?")


def handle_certificate(context):
    if not context:
        return "I need your login to check certificates. Please make sure you're signed in."
    conn = get_db()
    certs = conn.execute("""
        SELECT cert.*, c.title as course_title
        FROM certificates cert JOIN courses c ON cert.course_id = c.id
        WHERE cert.user_id=?
    """, (context["user"]["id"],)).fetchall()
    conn.close()

    if not certs:
        completed = [e for e in context["enrollments"] if e["completed"]]
        if completed:
            return (f"Congratulations on completing **{completed[0]['title']}**! "
                    "Your certificate is being processed and will be available soon. "
                    "You can download it from your dashboard once your trainer approves it.")
        return ("No certificates yet. Complete a course and pass the final assessment to earn your certificate!\n\n"
                f"Your progress: {len([e for e in context['enrollments'] if e['completed']])} courses completed.")

    response = "**Your Certificates**\n\n"
    for c in certs:
        response += f"- **{c['course_title']}** | ID: `{c['certificate_id']}` | Issued: {c['issued_at']}\n"
    return response


def handle_announcement(context):
    conn = get_db()
    anns = conn.execute("SELECT * FROM announcements ORDER BY rowid DESC LIMIT 5").fetchall()
    conn.close()

    if not anns:
        return "No recent announcements."

    response = "**Latest Announcements**\n\n"
    for a in anns:
        response += f"**{a['title']}**\n{a['content']}\n\n"
    return response


def handle_navigation(message):
    msg = message.lower()
    if "dashboard" in msg:
        return "**Navigation:** Head to your dashboard from the top menu. You'll see your enrolled courses, progress, and recent activity."
    if "course" in msg:
        return "**Navigation:** Go to **Courses** in the sidebar to browse or search all available courses."
    if "quiz" in msg:
        return "**Navigation:** Quizzes are inside each course module. Open a course and click on the quiz section."
    if "project" in msg:
        return "**Navigation:** Check the **Projects** section in your dashboard to view submissions and feedback."
    if "certificate" in msg:
        return "**Navigation:** Certificates are in the **Certification** section of your dashboard."
    if "announcement" in msg:
        return "**Navigation:** Latest announcements are displayed on your dashboard homepage."
    return "I can help you navigate! Tell me what you're looking for — dashboard, courses, quizzes, projects, or certificates."


def handle_question(message, context):
    msg = message.lower()

    if "what is" in msg or "what are" in msg:
        topic = msg.replace("what is", "").replace("what are", "").strip().rstrip("?")
        topic_key, subtopic_key = find_best_topic(topic)
        if topic_key:
            return teach_topic(topic_key, subtopic_key, detect_skill_level(message), detect_frustration(message))

        return (f"Great question about **{topic}**!\n\n"
                "Let me explain:\n\n"
                f"**{topic.title()}** is a concept that I'd love to explain in detail. "
                "To give you the best answer, could you tell me:\n"
                "1. Is this related to a specific course you're taking?\n"
                "2. What's your current level? (beginner/intermediate/advanced)\n"
                "3. What specifically about it confuses you?")

    topic_key, subtopic_key = find_best_topic(msg)
    if topic_key:
        return teach_topic(topic_key, subtopic_key, detect_skill_level(message), detect_frustration(message))

    return ("That's an interesting question! Let me think about the best way to explain this.\n\n"
            "Could you provide a bit more context?\n"
            "- Is this related to a specific course?\n"
            "- What's your current understanding of this topic?\n"
            "- What specifically would you like to know?")


def handle_general(message, context):
    msg = message.lower()

    if any(w in msg for w in ["thank", "thanks", "thank you"]):
        return "You're welcome! That's what I'm here for. Is there anything else you'd like to learn or practice?"

    if any(w in msg for w in ["who are you", "what are you", "your name"]):
        return ("I'm Sastra — your AI Learning Assistant for Capacity Connect.\n\n"
                "I'm designed to help you:\n"
                "❯ 🧠 Understand concepts (at your level)\n"
                "❯ 🎯 Practice with quizzes\n"
                "❯ 📊 Track your learning progress\n"
                "❯ 🧭 Get personalized recommendations\n"
                "❯ 📄 Create notes and PDF study materials\n"
                "❯ 🚀 Navigate the platform\n\n"
                "I adapt to your learning style and pace. Just ask me anything!")

    if any(w in msg for w in ["help", "what can you do"]):
        return ("I can help you with many things:\n\n"
                "Learning:\n"
                "❯ Explain concepts (Python, ML, React, Cloud, Security)\n"
                "❯ Teach at your skill level\n"
                "❯ Provide examples and practice questions\n\n"
                "Practice:\n"
                "❯ Quiz you on any topic\n"
                "❯ Review your answers and explain mistakes\n\n"
                "Platform:\n"
                "❯ Track your progress and quiz scores\n"
                "❯ Recommend courses and lessons\n"
                "❯ Help with projects and notes\n"
                "❯ Navigate the platform\n\n"
                "Just ask me anything!")

    return ("I'm here to help you learn! You can ask me to:\n\n"
            "❯ 📖 Teach a topic (e.g., 'Explain Python functions')\n"
            "❯ 🎯 Quiz me (e.g., 'Quiz me on machine learning')\n"
            "❯ 📊 Check my progress\n"
            "❯ 🧭 Recommend what to learn next\n"
            "❯ 📄 Help with a project or generate PDF\n\n"
            "What would you like to do?")


def process_message(message, user_id=None, user_name=None):
    context = get_user_context(user_id, custom_name=user_name)
    intent = detect_intent(message)
    skill_level = detect_skill_level(message)
    is_frustrated = detect_frustration(message)

    if intent == "greeting":
        return handle_greeting(context, message, custom_name=user_name)

    if intent == "teach":
        topic_key, subtopic_key = find_best_topic(message)
        if topic_key:
            return teach_topic(topic_key, subtopic_key, skill_level, is_frustrated)

    if intent == "quiz":
        return handle_quiz(message, context)

    if intent == "recommendation":
        return handle_recommendation(context)

    if intent == "progress":
        return handle_progress(context)

    if intent == "notes":
        return handle_notes(message, context)

    if intent == "project":
        return handle_project(context)

    if intent == "certificate":
        return handle_certificate(context)

    if intent == "announcement":
        return handle_announcement(context)

    if intent == "navigation":
        return handle_navigation(message)

    if intent == "question":
        return handle_question(message, context)

    return handle_general(message, context)
