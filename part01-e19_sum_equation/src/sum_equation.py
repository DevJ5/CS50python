#!/usr/bin/env python3
from functools import reduce


def sum_equation(L):

    if len(L) == 0:
        result = "0 = 0"
    else:
        sumL = reduce(lambda x, y: x + y, L, 0)
        result = (" + ").join([str(x) for x in L])
        result = (" = ").join([result, str(sumL)])

    return result


def main():
    print(sum_equation([]))


if __name__ == "__main__":
    main()
