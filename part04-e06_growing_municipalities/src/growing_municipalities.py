#!/usr/bin/env python3

import pandas as pd


def growing_municipalities(df):
    subset = df[(df["Population change from the previous year, %"] > 0)].index
    return subset.shape[0] / df.shape[0]


def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities = df["Akaa":"Äänekoski"]
    output = growing_municipalities(municipalities)
    print(f"Proportion of growing municipalities: {output * 100:.1f}%")


if __name__ == "__main__":
    main()
