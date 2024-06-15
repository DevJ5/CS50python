#!/usr/bin/env python3

import pandas as pd

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df["Suicides_Per_Population"] = df["suicides_no"] / df["population"]
    mean_fraction = df.groupby("country")["Suicides_Per_Population"].mean()
    
    return mean_fraction

def main():
    print(suicide_fractions())

if __name__ == "__main__":
    main()
