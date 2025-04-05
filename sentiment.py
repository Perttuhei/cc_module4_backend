import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

def sentiment(reviewText):
    df = pd.read_csv("train.csv", encoding="latin-1")
    df.dropna(inplace=True)
    X = df['text']
    y = df['sentiment']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    text_clf = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LinearSVC())
    ])

    text_clf.fit(X_train, y_train)
    predictions = text_clf.predict(X_test)
    # print(classification_report(y_test, predictions))
    # print(text_clf.predict(['This is wery bad! i hate this product. do not recommend']))
    response = text_clf.predict([reviewText])
    return response[0]