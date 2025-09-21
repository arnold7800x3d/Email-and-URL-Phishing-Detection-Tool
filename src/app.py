from flask import Flask, request, jsonify
from flask_cors import CORS
from src.inference.predict_email import predict_email
from src.inference.url_features import extract_url_features
import pandas as pd
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from werkzeug.security import generate_password_hash, check_password_hash
import joblib
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# ------------------ DATABASE CONFIG ------------------ #
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_PORT = int(os.getenv("DB_PORT"))

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

# ------------------ LOAD MODEL & SCALER ------------------ #
URL_MODEL_PATH = "backend/model_files/url_model.pkl"
SCALER_PATH = "backend/model_files/url_scaler.pkl"
FEATURE_COLUMNS_PATH = "backend/model_files/url_feature_columns.pkl"

lr_model = joblib.load(URL_MODEL_PATH)
scaler = joblib.load(SCALER_PATH)
feature_columns = joblib.load(FEATURE_COLUMNS_PATH)

# ------------------ ROUTES ------------------ #

@app.route('/')
def index():
    return "Phishing Detection API is running."

# Signup
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

# Login
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

# Predict email
@app.route('/predict/email', methods=['POST'])
def predict_email_route():
    data = request.get_json()
    email_text = data.get("email_text", "")
    if not email_text:
        return jsonify({"error": "No email text provided"}), 400
    
    result = predict_email(email_text)

    # Save to DB
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO phishguard_emails (email_text, prediction, probability) VALUES (%s, %s, %s);",
            (email_text, result['prediction'], result['probability'])
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("Error saving email record:", e)

    print(result)
    return jsonify(result)


# Predict URL
@app.route('/predict/url', methods=['POST'])
def predict_url_route():
    data = request.get_json()
    url = data.get("url", "")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # Extract features
    df_features = extract_url_features(url)

    # Ensure all features exist and match the trained model columns
    for col in feature_columns:
        if col not in df_features.columns:
            df_features[col] = 0
    df_features = df_features[feature_columns]

    # Scale features
    X_scaled = scaler.transform(df_features)

    # Predict
    prediction = lr_model.predict(X_scaled)[0]
    probability = lr_model.predict_proba(X_scaled)[0][prediction]

    result = {
        "prediction": "Phishing" if prediction == 0 else "Legitimate",
        "probability": float(probability)
    }

    # Save to DB
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO phishguard_urls (url, prediction, probability) VALUES (%s, %s, %s);",
            (url, result['prediction'], result['probability'])
        )
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print("Error saving URL record:", e)

    print(result)  # for debugging
    return jsonify(result)


# ------------------ RUN APP ------------------ #
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
