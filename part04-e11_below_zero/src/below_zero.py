#!/usr/bin/env python3

import pandas as pd

def below_zero():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    subset = df[df["Air temperature (degC)"] < 0]
    print(subset.shape[0])
    return len(subset.index)

def main():
    print(f"Number of days below zero: {below_zero()}")

if __name__ == "__main__":
    main()
