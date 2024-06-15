#!/usr/bin/env python3

import pandas as pd


def best_record_company():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    grouped_df = df.groupby("Publisher")["WoC"].sum()
    max_weeks = grouped_df.idxmax()
    return df[df["Publisher"] == max_weeks]

    # Can also be done with sorting and taking the first value
    # grouped_df = grouped_df.sort_values(ascending=False)
    # top_publisher = grouped_df.index[0]


def main():
    print(best_record_company())


if __name__ == "__main__":
    main()
