#!/usr/bin/env python3

import pandas as pd


def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    municipalities = df["Akaa":"Äänekoski"]
    subset = municipalities[
        (municipalities["Share of Swedish-speakers of the population, %"] > 5)
        & (municipalities["Share of foreign citizens of the population, %"] > 5)
    ]
    subset = subset[
        [
            "Population",
            "Share of Swedish-speakers of the population, %",
            "Share of foreign citizens of the population, %",
        ]
    ]
    return subset


def main():
    print(swedish_and_foreigners())


if __name__ == "__main__":
    main()
