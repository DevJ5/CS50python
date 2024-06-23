#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer

alphabet = "abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)


# Returns a list of Finnish words
def load_finnish():
    finnish_url = "https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename = "src/kotus-sanalista_v1.xml"
    load_from_net = False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines = []
            for line in data:
                lines.append(line.decode("utf-8"))
        doc = "".join(lines)
    else:
        with open(filename, "rb") as data:
            doc = data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath("/kotus-sanalista/st/s")
    return list(map(lambda s: s.text, s_elements))


def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines = map(lambda s: s.rstrip(), data.readlines())
    return lines


def get_features(a):
    # Custom tokenizer function to tokenize into characters
    def char_tokenizer(text):
        return list(text)

    # Initialize CountVectorizer with custom tokenizer
    vectorizer = CountVectorizer(analyzer="char", vocabulary=alphabet_set)

    # Fit to the data and transform to get the sparse matrix
    X = vectorizer.fit_transform(a)

    # Print feature names (vocabulary)
    print("Feature names (vocabulary):")
    print(vectorizer.get_feature_names_out())

    # Turn sparse matrix into np array
    X = X.toarray()

    # '-' is now in the first index. We need to get this column which is 1d and append it to the end.
    X = np.hstack((X[:, 1:], X[:, 0].reshape(-1, 1)))
    return X


def contains_valid_chars(s):
    for c in s:
        if c not in alphabet_set:
            return False
    return True


def get_features_and_labels():
    finnish = load_finnish()
    finnish = [word.lower() for word in finnish]
    finnish = [word for word in finnish if contains_valid_chars(word)]

    english = list(load_english())
    english = [word.lower() for word in english if word[0].islower()]
    english = [word for word in english if contains_valid_chars(word)]

    finnish_features = get_features(finnish)
    finnish_target = np.zeros((len(finnish), 1))
    english_features = get_features(english)
    english_target = np.ones((len(english), 1))

    features = np.vstack((finnish_features, english_features))
    target = np.vstack((finnish_target, english_target)).ravel()

    return (features, target)


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    scores = cross_val_score(model, X, y, cv=5)
    print(scores)

    generator = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(model, X, y, cv=generator)

    return scores


def main():
    print("Accuracy scores are:", word_classification())


if __name__ == "__main__":
    main()
