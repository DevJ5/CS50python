#!/usr/bin/env python3
import gzip
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


def spam_detection(random_state=0, fraction=1.0):
    ham, spam = [], []
    file_path_ham, file_path_spam = "src/ham.txt.gz", "src/spam.txt.gz"

    with gzip.open(file_path_ham, "r") as file:
        lines = file.readlines()
        total_lines = len(lines)
        start_index = 0
        end_index = int(total_lines * fraction)
        ham = ham + lines[start_index:end_index]

    with gzip.open(file_path_spam, "r") as file:
        lines = file.readlines()
        total_lines = len(lines)
        start_index = 0
        end_index = int(total_lines * fraction)
        spam = spam + lines[start_index:end_index]

    emails = ham + spam
    labels = [0] * len(ham) + [1] * len(spam)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(emails)

    feature_names = vectorizer.get_feature_names_out()
    X_dense = X.toarray()
    print("Feature Names:")
    print(feature_names)
    print("Feature Matrix:")
    print(X_dense)

    X_train, X_test, y_train, y_test = train_test_split(
        X, labels, test_size=0.25, random_state=random_state
    )

    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    # Predictions
    y_pred = clf.predict(X_test)

    # Evaluation
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    accuracy = accuracy_score(y_test, y_pred)
    misclassified_samples = (y_test != y_pred).sum()

    return accuracy, len(y_test), misclassified_samples


def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")


if __name__ == "__main__":
    main()
