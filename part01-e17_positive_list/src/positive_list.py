#!/usr/bin/env python3


def positive_list(L):
    positiveNumbers = list(filter(lambda x: x > 0, L))
    return positiveNumbers


def main():
    positive_list([2, -2, 0, 1, -7])


if __name__ == "__main__":
    main()
