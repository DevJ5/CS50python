#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns

sns.set(color_codes=True)
import scipy
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc
import re


def toint(x):
    translations = {"A": 0, "C": 1, "G": 2, "T": 3}
    return translations[x]


def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep="\t")
    X = df["X"].apply(lambda s: [toint(char) for char in s])
    X = np.array(X.tolist())
    y = df.loc[:, "y"]

    return (X, y)


def plot(distances, method="average", affinity="euclidean"):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g = sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage)
    g.fig.suptitle(
        f"Hierarchical clustering using {method} linkage and {affinity} affinity"
    )
    plt.show()


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation


def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(
        n_clusters=2, linkage="average", affinity="euclidean"
    )
    model.fit(X)

    permutation = find_permutation(2, y, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]  # permute the labels

    acc_score = accuracy_score(y, new_labels)
    return acc_score


def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    distance = pairwise_distances(X, metric="hamming")
    model = AgglomerativeClustering(
        n_clusters=2, linkage="average", affinity="precomputed"
    )
    model.fit_predict(distance)

    permutation = find_permutation(2, y, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]  # permute the labels

    acc_score = accuracy_score(y, new_labels)
    return acc_score


def main():
    print(
        "Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq")
    )
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))


if __name__ == "__main__":
    main()
