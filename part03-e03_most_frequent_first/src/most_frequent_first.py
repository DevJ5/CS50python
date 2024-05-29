#!/usr/bin/env python3

import numpy as np


# that gets a two dimensional array and an index c of a column as parameters
def most_frequent_first(a, c):
    column = a[:, c]
    print(column)
    value, count = np.unique(column, return_counts=True)
    print(value, count)

    indexes_count_desc = np.argsort(-count)
    print(indexes_count_desc)
    values_desc = value[indexes_count_desc].reshape((1, -1))
    print(values_desc)

    indexes = np.concatenate([np.where(column == x)[0] for x in np.nditer(values_desc)])
    print(a[indexes])
    return a[indexes]


def main():
    # Test with this 9 by 9 matrix and the last column
    most_frequent_first(
        np.array(
            [
                [5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
                [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
                [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
                [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
                [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
                [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
                [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
                [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
                [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
                [5, 9, 3, 0, 5, 0, 1, 2, 4, 2],
            ]
        ),
        -1,
    )


if __name__ == "__main__":
    main()
