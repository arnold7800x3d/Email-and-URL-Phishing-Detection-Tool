import joblib
import numpy as np

# path to vectorizer file
VECTORIZER_PATH = "backend/model_files/email_vectorizer.pkl"

def main():
    # load vectorizer
    vectorizer = joblib.load(VECTORIZER_PATH)
    
    # get feature names
    feature_names = vectorizer.get_feature_names_out()
    
    print(f"Total number of features: {len(feature_names)}\n")
    
    # display the first 20 features
    print("First 20 features:")
    print(feature_names[:20])
    
    # show top features by inverse document frequency
    idf_values = vectorizer.idf_
    top_indices = np.argsort(idf_values)[:20]  # lowest IDF = most frequent words
    top_features = feature_names[top_indices]
    top_idf = idf_values[top_indices]
    
    print("\nTop 20 most frequent words (lowest IDF):")
    for word, idf in zip(top_features, top_idf):
        print(f"{word}: {idf:.4f}")

if __name__ == "__main__":
    main()
