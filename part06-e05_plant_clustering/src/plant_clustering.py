#!/usr/bin/env python3

import scipy
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import pandas as pd


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation


def plant_clustering():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    print(df.head())
    # Initialize the KMeans object with 3 clusters (since we know there are 3 species)
    model = KMeans(n_clusters=3, random_state=0)
    # Fit the KMeans model to the data
    model.fit(df)
    # Print the cluster centers
    print("Cluster centers:")
    print(model.cluster_centers_)
    # Print the cluster labels (assigned to each data point)
    print("\nCluster labels:")
    print(model.labels_)

    permutation = find_permutation(3, iris.target, model.labels_)
    acc = accuracy_score(iris.target, [permutation[label] for label in model.labels_])
    print("Accuracy score is", acc)

    return acc


def main():
    print(plant_clustering())


if __name__ == "__main__":
    main()
