# Email and URL Phishing Detection Tool
## Creating a virtual environment
To manage libraries for the project separate from the local python interpreter, create a virtual environment.
In the project terminal, run the following sequence of commands.
```
python -m venv venv 
``` 
To activate the environment on Windows:
```
venv\Scripts\activate
```
The terminal prompt now changes as it is pre-pended with (venv).

## Installing dependencies
To install initial dependencies for preprocessing and modelling:
```
pip install pandas numpy scikit-learn flask joblib
```

## Training the Naive Bayes email classifier model
In the project root, run:
```
python -m src.models.train_email_model
```

The output:
```
Loaded 2000 emails.
Email feature matrix shape: (2000, 163)
Vectorizer saved to backend/model_files/email_vectorizer.pkl       
Training samples: 1600, Test samples: 400
Naive Bayes model trained successfully

Evaluation Metrics
Accuracy: 1.0000
Precision: 1.0000
Recall: 1.0000
F1 Score: 1.0000

Classification Report:
                precision    recall  f1-score   support

    Safe Email       1.00      1.00      1.00       211
Phishing Email       1.00      1.00      1.00       189

      accuracy                           1.00       400
     macro avg       1.00      1.00      1.00       400
  weighted avg       1.00      1.00      1.00       400

Trained model saved to backend/model_files/email_model.pkl
```
The perfomance evaluates to 100% accuracy, mostly because the dataset is small and well balanced.

To view the features used in vectorization, run in the project root:
```
python src/utils/visualize_email_features.py
```

The output:
```
Total number of features: 163

First 20 features:
['about' 'account' 'activity' 'alert' 'alex' 'am' 'and' 'any' 'are' 'at'
 'attached' 'attempt' 'avoid' 'bank' 'be' 'been' 'billing' 'by' 'card'
 'casey']

Top 20 most frequent words (lowest IDF):
your: 1.2895
to: 1.6002
the: 2.0575
you: 2.1653
our: 2.1962
is: 2.2061
for: 2.2128
please: 2.2247
dear: 2.5755
review: 2.6150
here: 2.6301
account: 2.6665
about: 2.7993
hi: 2.8114
attached: 2.8616
has: 2.8713
been: 2.8713
click: 2.8778
meeting: 2.8943
update: 2.9281
```

## Training the Logistic Regression URL model
To train the logistic regression model, run:
```
python -m src.models.train_url_model
```

The output:
```
Loaded 235795 URLs.
Feature matrix shape before scaling: (235795, 51)
Scaler saved to backend/model_files/url_scaler.pkl
Training samples: 188636, Test samples: 47159
Logistic Regression model trained successfully.

--- Evaluation Metrics ---
Accuracy: 1.0000
Precision: 1.0000
Recall: 1.0000
F1 Score: 1.0000

Classification Report:
              precision    recall  f1-score   support

  Legitimate       1.00      1.00      1.00     20124
    Phishing       1.00      1.00      1.00     27035

    accuracy                           1.00     47159
   macro avg       1.00      1.00      1.00     47159
weighted avg       1.00      1.00      1.00     47159

Trained Logistic Regression model saved to backend/model_files/url_model.pkl
```

The model achieves perfect accuracy, due to the characteristics of the datasets, since the feature matrix reveals that all the numeric features are included.