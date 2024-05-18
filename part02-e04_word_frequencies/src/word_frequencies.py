#!/usr/bin/env python3

import string


def word_frequencies(filename):
    result = {}

    with open(filename, "r") as in_file:
        for line in in_file:
            words = map(lambda w: w.strip(string.punctuation), line.split())
            for word in words:
                if word in result:
                    result[word] = result[word] + 1
                else:
                    result[word] = 1

    return result


def main():
    word_frequencies("src/alice.txt")


if __name__ == "__main__":
    main()
