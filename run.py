import pandas as pd

URL_DATA_PATH = "data/PhiUSIIL_Phishing_URL_Dataset.csv"
data = pd.read_csv(URL_DATA_PATH)

# Count values for each label
print(data['label'].value_counts())

# Look at a few samples from each label
print("\n--- Label 0 samples ---")
print(data[data['label'] == 0]['URL'].head(5))

print("\n--- Label 1 samples ---")
print(data[data['label'] == 1]['URL'].head(5))
