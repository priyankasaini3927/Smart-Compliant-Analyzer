from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

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
x_test_vectorized = vectorizer.transform(x_test)


logistic_accuracy = LogisticRegression()
logistic_accuracy.fit(x_train_vectorized, y_train)
logistic_pred = logistic_accuracy.predict(x_test_vectorized)
logistic_accuracy = accuracy_score(y_test, logistic_pred)


nb_accuracy = MultinomialNB()
nb_accuracy.fit(x_train_vectorized, y_train)
nb_pred = nb_accuracy.predict(x_test_vectorized)
nb_accuracy = accuracy_score(y_test, nb_pred)

print("Logistic:", logistic_accuracy)
print("Naive Bayes:", nb_accuracy)