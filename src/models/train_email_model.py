import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
import joblib
from src.preprocessing.email_preprocessing import EmailPreprocessor, load_email_data, split_data

# configuration
EMAIL_DATA_PATH = "data/Phishing_validation_emails.csv"
MODEL_SAVE_PATH = "backend/model_files/email_model.pkl"
VECTORIZER_SAVE_PATH = "backend/model_files/email_vectorizer.pkl"
TEST_SIZE = 0.2
RANDOM_STATE = 42

# load data
X_raw, y = load_email_data(EMAIL_DATA_PATH)
print(f"Loaded {len(X_raw)} emails.")

# preprocess the data
preprocessor = EmailPreprocessor(vectorizer_type = 'tfidf', max_features = 5000)
X_features = preprocessor.fit_transform(X_raw)
print(f"Email feature matrix shape: {X_features.shape}")

# save the vectorizer
preprocessor.save_vectorizer(VECTORIZER_SAVE_PATH)
print(f"Vectorizer saved to {VECTORIZER_SAVE_PATH}")

# split data
X_train, X_test, y_train, y_test = split_data(X_features, y, test_size = TEST_SIZE, random_state = RANDOM_STATE)
print(f"Training samples: {X_train.shape[0]}, Test samples: {X_test.shape[0]}")

# train naive bayes classifier
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
print("Naive Bayes model trained successfully")

# evaluate model
y_pred = nb_model.predict(X_test)

print("\nEvaluation Metrics")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall: {recall_score(y_test, y_pred):.4f}")
print(f"F1 Score: {f1_score(y_test, y_pred):.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Safe Email', 'Phishing Email']))

# save trained model
joblib.dump(nb_model, MODEL_SAVE_PATH)
print(f"Trained model saved to {MODEL_SAVE_PATH}")