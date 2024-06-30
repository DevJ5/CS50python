#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def explained_variance():
    df = pd.read_csv("src/data.tsv", sep="\t")
    # Calculating the variance of all features
    variance = df.var()
    variance = variance.to_numpy()
    # Performing PCA on the dataset
    pca = PCA()
    pca.fit(df)
    # Extracting the variance explained by each principal component
    explained_variance = pca.explained_variance_

    return variance, explained_variance


def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    v_str_list = " ".join([f"{x:.3f}" for x in v])
    ev_str_list = " ".join([f"{x:.3f}" for x in ev])

    print(f"The variances are: {v_str_list}")
    print(f"The explained variances after PCA are: {ev_str_list}")

    plt.plot(np.arange(1, 11), np.cumsum(ev))
    plt.show()


if __name__ == "__main__":
    main()
