from flask import Flask, request, jsonify
from flask_cors import CORS
from src.inference.predict_email import predict_email
from src.inference.predict_url import predict_url
import pandas as pd
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

# database connection
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "phishing_app")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASS", "7800")
DB_PORT = os.environ.get("DB_PORT", 5432)

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT,
        cursor_factory=RealDictCursor
    )
    return conn

# signup route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not all([name, email, password]):
        return jsonify({"error": "Missing fields"}), 400

    hashed_password = generate_password_hash(password)

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id;",
            (name, email, hashed_password)
        )
        user_id = cur.fetchone()['id']
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "User created successfully", "user_id": user_id}), 201
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        return jsonify({"error": "Email already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# login route
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return jsonify({"error": "Missing email or password"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s;", (email,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and check_password_hash(user['password'], password):
            return jsonify({"message": f"Welcome, {user['name']}!"})
        else:
            return jsonify({"error": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# routes

@app.route('/')
def index():
    return "Phishing Detection API is running."

@app.route('/predict/email', methods=['POST'])
def predict_email_route():
    """
    expects a JSON
    {
        "email_text": "string"
    }
    """
    data = request.get_json()
    email_text = data.get("email_text," "")
    if not email_text:
        return jsonify({"error": "No email text provided"}), 400
    
    result = predict_email(email_text)
    return jsonify(result)

@app.route('/predict/url', methods=['POST'])
def predict_url_route():
    """
    Expects JSON with numeric URL features matching training columns, e.g.:
    {
        "URLLength": 31,
        "DomainLength": 24,
        "IsDomainIP": 0,
        ...
    }
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No URL features provided"}), 400

    # convert input dict to single-row DataFrame
    try:
        df_features = pd.DataFrame([data])
    except Exception as e:
        return jsonify({"error": f"Invalid data format: {e}"}), 400

    result = predict_url(df_features)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

