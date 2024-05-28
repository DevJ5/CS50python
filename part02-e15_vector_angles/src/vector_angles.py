#!/usr/bin/env python3

import numpy as np
import scipy.linalg


def vector_angles(X, Y):
    dotproduct = np.sum(X * Y)
    magX = np.sqrt(np.sum(X**2))
    magY = np.sqrt(np.sum(Y**2))
    return dotproduct / (magX * magY)


def main():
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])
    z = np.array([x, y])

    print(vector_angles(x, y))


if __name__ == "__main__":
    main()
