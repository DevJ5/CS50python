#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    # Load the Iris dataset
    iris = load_iris()

    # Print the description of the dataset
    print(iris.DESCR)

    # Accessing feature names
    print("\nFeature names:")
    print(iris.feature_names)

    # Accessing target names
    print("\nTarget names:")
    print(iris.target_names)

    # Accessing data (feature matrix X) and target (label vector y)
    X = iris.data   # feature matrix (numpy array)
    y = iris.target   # label vector (numpy array)

    # Print shape of X and y
    print("\nShape of X:", X.shape)
    print("Shape of y:", y.shape)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0
    )

    # Initialize Gaussian Naive Bayes model
    model = naive_bayes.GaussianNB()

    # Fit the model on the training data
    model.fit(X_train, y_train)

    # Predict on the test data
    y_pred = model.predict(X_test)
    print(y_pred)

    # Evaluate model performance
    accuracy = metrics.accuracy_score(y_test, y_pred)
    return accuracy

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
