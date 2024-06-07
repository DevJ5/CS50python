#!/usr/bin/env python3

import pandas as pd


def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    subset = df.dropna(how="all")
    subset = subset.dropna(axis=1, how="all")
    return subset


def main():
    cyclists()


if __name__ == "__main__":
    main()
