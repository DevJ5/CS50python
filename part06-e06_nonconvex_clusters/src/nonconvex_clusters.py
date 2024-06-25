#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import scipy


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep="\t")
    # EDA
    print(df.head())
    print(df.shape)
    print(df.info())
    print(df.describe())
    print("---------------------------- END EDA ----------------------------")

    # Train model
    X, y = df.iloc[:, :-1].values, df.iloc[:, -1].values
    num_clusters_y = len(set(y))
    result = []

    for v in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=v)
        model.fit(X)

        # Count unique labels, ignoring noise (-1)
        num_clusters = len(set(model.labels_)) - (1 if -1 in model.labels_ else 0)
        num_noise = list(model.labels_).count(-1)

        permutation = find_permutation(num_clusters, y, model.labels_)
        new_labels = [
            permutation[label] for label in model.labels_
        ]  # permute the labels

        if num_clusters_y != num_clusters:
            acc_score = None
        else:
            noise_mask = model.labels_ == -1
            # new_labels is a list, we need a numpy array to use masking
            acc_score = accuracy_score(y[~noise_mask], np.array(new_labels)[~noise_mask])

        # plt.figure(figsize=(8, 6))
        # plt.scatter(X[:, 0], X[:, 1], c=model.labels_)
        # plt.show()

        result.append([v, acc_score, num_clusters, num_noise])

    df = pd.DataFrame(
        result, columns=["eps", "Score", "Clusters", "Outliers"], dtype=float
    )
    return df


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
