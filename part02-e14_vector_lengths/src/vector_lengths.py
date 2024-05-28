#!/usr/bin/env python3

import numpy as np

# import scipy.linalg


def vector_lengths(a):
    result = np.sqrt((a**2).sum(axis=1))
    return result


def main():
    vector_lengths(np.array([[1, 2], [3, 4]]))


if __name__ == "__main__":
    main()
