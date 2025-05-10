import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = pd.read_csv('https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv', sep='\t', header=None, names=['label', 'message'])

data['label_num'] = data.label.map({'ham': 0, 'spam': 1})

X = data['message']
y = data['label_num']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

sample_messages = [
    "Congratulations! You've won a free ticket to Bahamas! Call now.",
    "Hey, are we still on for lunch today?",
    "Get cheap loans now with no documents required!",
    "I'll send you the meeting notes shortly."
]

sample_vec = vectorizer.transform(sample_messages)
predictions = model.predict(sample_vec)

for message, label in zip(sample_messages, predictions):
    print(f"'{message}' --> {'Spam' if label == 1 else 'Ham'}")
