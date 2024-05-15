#!/usr/bin/env python3


def transform(s1, s2):
    # result = []
    # s1Ints = list(map(int, s1.split()))
    # s2Ints = list(map(int, s2.split()))

    # zippedList = list(zip(s1Ints, s2Ints))
    # result = list(map(lambda x: x[0] * x[1], zippedList))

    # return result

    return [x * y for (x, y) in zip(map(int, s1.split()), map(int, s2.split()))]


def main():
    print(transform("1 5 3", "2 6 -1"))


if __name__ == "__main__":
    main()
