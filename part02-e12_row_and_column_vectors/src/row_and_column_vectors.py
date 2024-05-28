#!/usr/bin/env python3

import numpy as np


def get_row_vectors(a):
    result = []
    rows_number, col_number = np.shape(a)

    return np.vsplit(a, rows_number)


def get_column_vectors(a):
    result = []
    for column in a.T:
        result.append(column.reshape(len(column), 1))
    return result


def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (4, 4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))


if __name__ == "__main__":
    main()
