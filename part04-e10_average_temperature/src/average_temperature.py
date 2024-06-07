#!/usr/bin/env python3

import pandas as pd


def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    df_july = df[df.m == 7]
    print(df_july.describe())
    subset = df[df["m"] == 7]["Air temperature (degC)"].mean()
    return subset


def main():
    print(f"Average temperature in July: {average_temperature():.1f}")


if __name__ == "__main__":
    main()
