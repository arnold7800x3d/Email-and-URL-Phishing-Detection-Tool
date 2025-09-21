import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import joblib

# configuration
URL_DATA_PATH = "data/PhiUSIIL_Phishing_URL_Dataset.csv"
MODEL_SAVE_PATH = "backend/model_files/url_model.pkl"
SCALER_SAVE_PATH = "backend/model_files/url_scaler.pkl"
FEATURES_SAVE_PATH = "backend/model_files/url_feature_columns.pkl"
TEST_SIZE = 0.2
RANDOM_STATE = 42

# load data
data = pd.read_csv(URL_DATA_PATH)
print(f"Loaded {len(data)} URLs.")

# feature selection
features = [
    'URLLength', 'DomainLength', 'IsDomainIP', 'TLDLength', 'NoOfSubDomain',
    'NoOfLettersInURL', 'LetterRatioInURL', 'NoOfDegitsInURL', 'DegitRatioInURL',
    'NoOfEqualsInURL', 'NoOfQMarkInURL', 'NoOfAmpersandInURL', 'NoOfOtherSpecialCharsInURL',
    'SpacialCharRatioInURL', 'NoOfObfuscatedChar', 'HasObfuscation', 'ObfuscationRatio',
    'IsHTTPS', 'Bank', 'Pay', 'Crypto'
]

X = data[features]
y = data['label']  # 0 = phishing, 1 = legitimate

print(f"Feature matrix shape before scaling: {X.shape}")

# save feature column order for inference
feature_columns = X.columns.tolist()
joblib.dump(feature_columns, FEATURES_SAVE_PATH)
print(f"Feature columns saved to {FEATURES_SAVE_PATH}")

# scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# save the scaler for inference
joblib.dump(scaler, SCALER_SAVE_PATH)
print(f"Scaler saved to {SCALER_SAVE_PATH}")

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=TEST_SIZE, random_state=RANDOM_STATE
)
print(f"Training samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

# train logistic regression model
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train, y_train)
print("Logistic Regression model trained successfully.")

# evaluate model
y_pred = lr_model.predict(X_test)

print("\n--- Evaluation Metrics ---")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, pos_label=0):.4f} (phishing)")
print(f"Recall: {recall_score(y_test, y_pred, pos_label=0):.4f} (phishing)")
print(f"F1 Score: {f1_score(y_test, y_pred, pos_label=0):.4f} (phishing)")

print("\nClassification Report:")
print(classification_report(
    y_test, y_pred, target_names=['Phishing (0)', 'Legitimate (1)']
))

# save the trained model
joblib.dump(lr_model, MODEL_SAVE_PATH)
print(f"Trained Logistic Regression model saved to {MODEL_SAVE_PATH}")
