#!/usr/bin/env python3
from functools import reduce
import numpy as np


def matrix_power(m, n):
    if n == 0:
        return np.eye(m.shape[0])
    elif n < 0:
        m = np.linalg.inv(m)
        n = -1 * n

    genM = (m for i in range(n))
    return reduce(lambda x, y: x @ y, genM)


def main():
    print(matrix_power(np.array([[1, 2], [3, 4]]), 0))


if __name__ == "__main__":
    main()
