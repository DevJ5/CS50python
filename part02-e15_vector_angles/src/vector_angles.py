#!/usr/bin/env python3

import numpy as np
import scipy.linalg


def vector_angles(X, Y):
    result = np.zeros(X.shape[0])

    for i in range(X.shape[0]):
        dotproduct = np.sum(X[i] * Y[i])
        magX = np.sqrt(np.sum(X[i] ** 2))
        magY = np.sqrt(np.sum(Y[i] ** 2))
        result[i] = dotproduct / (magX * magY)

        # Alternative
        # result[i] = np.dot(X[i], Y[i])/(scipy.linalg.norm(X[i])*scipy.linalg.norm(Y[i]))

    result = np.clip(result, -1, 1)
    return np.degrees(np.arccos(result))


def main():
    # A vector has m dimensions
    # An array has n,m shape, which is a 2d array
    # Each row in the 2d array, which is n, is a vector of m dimension

    # 1 Row example
    x = np.array([[1, 2, 3]])
    y = np.array([[4, 5, 6]])

    print(vector_angles(x, y))


if __name__ == "__main__":
    main()
