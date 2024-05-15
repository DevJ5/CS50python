#!/usr/bin/env python3


def distinct_characters(L):
    result = {}
    for str in L:
        result[str] = len(set(str))

    return result


def main():
    print(distinct_characters(["check", "look", "try", "pop"]))


if __name__ == "__main__":
    main()
