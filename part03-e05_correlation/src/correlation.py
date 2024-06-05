#!/usr/bin/env python3

import scipy.stats
import numpy as np
import pandas as pd


def load():

    return pd.read_csv("src/iris.csv").drop("species", axis=1).values


def lengths():
    df = load()
    sepal_length = df[:, 0]
    petal_length = df[:, 2]
    corr_coef, p_value = scipy.stats.pearsonr(sepal_length, petal_length)
    return corr_coef


def correlations():
    df = load()
    return np.corrcoef(df, rowvar=False)


def main():
    print(lengths())
    print(correlations())


if __name__ == "__main__":
    main()
