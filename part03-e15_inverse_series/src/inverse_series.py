#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    print(s.values)
    print(s.index)
    return pd.Series(s.index,index=s.values)

def main():
    print(inverse_series(pd.Series([1, 2, 3])))

if __name__ == "__main__":
    main()
