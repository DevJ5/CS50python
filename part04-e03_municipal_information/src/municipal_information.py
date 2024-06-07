#!/usr/bin/env python3

import pandas as pd

def main():
    df = pd.read_csv("src/municipal.tsv", delimiter="\t")
    print(f"Shape: {df.shape[0]}, {df.shape[1]}")
    print(f"Columns:")
    for c in df.columns:
        print(c)
    


if __name__ == "__main__":
    main()
