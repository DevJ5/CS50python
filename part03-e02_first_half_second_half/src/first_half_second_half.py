#!/usr/bin/env python3

import numpy as np


# two dimensional array of shape (n,2*m) as parameter a
def first_half_second_half(a):
    column_count = a.shape[1]
    # Integer division otherwise slice doesn't work
    m = column_count // 2
    # sum of the first m elements larger than the sum of the last m elements on the row
    b = np.sum(a[:, 0:m], axis=1) > np.sum(a[:, m:], axis=1)
    return a[b]


def main():
    a = np.array([[1, 3, 4, 2], [2, 2, 1, 2]])
    first_half_second_half(a)


if __name__ == "__main__":
    main()
