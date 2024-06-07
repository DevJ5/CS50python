#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    subset = df[~df["LW"].isin(["New", "Re"])]
    # Because Pos has only integers, its type is considered int
    # Because LW has New and Re, its type is considered str
    subset = subset[subset["Pos"] > subset["LW"].astype(int)]

    return subset


def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
