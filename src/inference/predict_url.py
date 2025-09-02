import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

# paths
MODEL_PATH = "backend/model_files/url_model.pkl"
SCALER_PATH = "backend/model_files/url_scaler.pkl"

# load model and scaler
url_model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_url(url_features: pd.DataFrame):
    """
    predicts if a URL is phishing or legitimate
    arguments
        url_features (pd.DataFrame): Dataframe with same numeric columns as training features
    output
        dictionary: {'prediction': 'Phishing'/'Legitimate', 'probability': float}
    """
    # scale features
    X_scaled = scaler.transform(url_features)

    # predict 
    predicted_class = url_model.predict(X_scaled)[0]
    predicted_probability = url_model.predict_proba(X_scaled)[0][predicted_class]

    result = {
        'prediction': 'Phishing' if predicted_class == 1 else 'Legitimate',
        'probability': float(predicted_probability)
    }
    return result
