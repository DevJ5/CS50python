#!/usr/bin/env python3

import pandas as pd


def read_series():
    indexes = []
    values = []
    while True:
        inp = input("Give index and value: ")
        if inp == "":
            break
        else:
            inpSplit = inp.split()
            print(inpSplit)
            if len(inpSplit) <= 1:
                raise Exception
            else:
                indexes.append(inpSplit[0])
                values.append("".join(inpSplit[1:]))

    s = pd.Series(values, index=indexes)
    return s


def main():
    print(read_series())
    print("".join(["b", "", "", "", "", "", "3"][1:]))


if __name__ == "__main__":
    main()
