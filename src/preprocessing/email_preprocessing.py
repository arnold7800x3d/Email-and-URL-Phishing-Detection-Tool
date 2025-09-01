import pandas as pd
import re
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
import joblib

class EmailPreprocessor:
    def __init__(self, vectorizer_type = 'tfidf', max_features = 5000):
        """
        initialize the email preprocessor
        parameters
            vectorizer_type: tfidf or cound
            max_features: maximum number of features for the vectorizer
        """
        if vectorizer_type == 'tfidf':
            self.vectorizer = TfidfVectorizer(max_features = max_features)
        else:
            self.vectorizer = CountVectorizer(max_features = max_features)

    @staticmethod
    def clean_text(text):
        # clean email text - remove HTML tags, URLs, punctuation, numbers, etc

        # have text as lowercase
        text = text.lower()

        # remove urls
        text = re.sub(r'http\S+|www\S+', '', text)

        # remove HTML tags
        text = re.sub(r'<.*?>', '', text)

        # remove numbers
        text = re.sub(r'\d+', '', text)

        # remove punctuation marks
        text = text.translate(str.maketrans('', '', string.punctuation))

        # remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    def fit_transform(self, texts):
        # fit vectorizer on training texts and transform into a feature matrix

        cleaned = [self.clean_text(t) for t in texts]
        X = self.vectorizer.fit_transform(cleaned)
        return X
    
    def transform(self, texts):
        # transform new texts into the trained vectorizer space

        cleaned = [self.clean_text(t) for t in texts]
        X = self.vectorizer.transform(cleaned)
        return X
    
    def save_vectorizer(self, path):
        joblib.dump(self.vectorizer, path)

    def load_vectorizer(self, path):
        self.vectorizer = joblib.load(path)

def load_email_data(file_path):
    # load email dataset and return features and labels
    data = pd.read_csv(file_path)
    X = data['Email Text']
    y = data['Email Type'].map({'Safe Email': 0, 'Phishing Email': 1}) # encoding labels
    return X, y

def split_data(X, y, test_size = 0.2, random_state = 42):
    # split data into training and testing sets

    return train_test_split(X, y, test_size = test_size, random_state = random_state)