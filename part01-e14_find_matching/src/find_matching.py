#!/usr/bin/env python3


def find_matching(L, pattern):
    # L = List of strings
    # pattern = search string

    result = []
    for i, str in enumerate(L):
        if pattern in str:
            result.append(i)

    return result


def main():
    find_matching(["sensitive", "engine", "rubbish", "comment"], "en")


if __name__ == "__main__":
    main()
