#!/usr/bin/env python3

import pandas as pd
import numpy as np


def powers_of_series(s, k):
    df = pd.DataFrame(index=s.index)
    for i in range(1, k + 1):
        df[i] = [x**i for x in s]

    return df


def main():
    s = pd.Series([1, 2, 3, 4], index=list("abcd"))
    print(powers_of_series(s, 3))


if __name__ == "__main__":
    main()
