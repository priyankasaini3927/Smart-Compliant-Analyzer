import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv("data/complaints.csv")
print(len(df))

X = df["text"]
y = df["category"]

vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)

model.fit(X_vectorized, y)

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model Trained")


vectorizer = joblib.load("app/vectorizer.pkl")

print("pothole" in vectorizer.vocabulary_)
print("transformer" in vectorizer.vocabulary_)
print("bus" in vectorizer.vocabulary_)