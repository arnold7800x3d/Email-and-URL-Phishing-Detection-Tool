import joblib
import os
from src.preprocessing.email_preprocessing import EmailPreprocessor

# paths
MODEL_PATH = "backend/model_files/email_model.pkl"
VECTORIZER_PATH = "backend/model_files/email_vectorizer.pkl"

# load model and vectorizer
email_model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# initialize preprocessor
preprocessor = EmailPreprocessor()
preprocessor.load_vectorizer(VECTORIZER_PATH)

def predict_email(email_text: str):
    """
    predicts if an email is phishing is legit
    arguments:
        email_text (str): raw email content
    output:
        dictionary: {'prediction': 'Safe Email'/'Phishing Email', 'probability': float}
    """
    # transform email text
    X_features = preprocessor.transform([email_text])

    # predicct
    predicted_class = email_model.predict(X_features)[0]
    predicted_probability = email_model.predict_proba(X_features)[0][predicted_class]

    result = {
        'prediction': 'Phishing email' if predicted_class ==1 else 'Safe Email',
        'probability': float(predicted_probability)
    }

    return result


