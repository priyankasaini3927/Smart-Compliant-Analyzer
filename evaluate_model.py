import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


df = pd.read_csv("data/complaints.csv")

x = df["text"]
y = df["category"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

vectorizer = TfidfVectorizer()
x_train_vectorized = vectorizer.fit_transform(x_train)
model = LogisticRegression()
model.fit(x_train_vectorized, y_train)
x_test_vectorized = vectorizer.transform(x_test)
prediction = model.predict(x_test_vectorized)
accuracy = accuracy_score(y_test, prediction)
print(f"Model Accuracy: {accuracy:.2f}")
print(df["category"].value_counts())
print(classification_report(y_test, prediction))