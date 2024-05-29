#!/usr/bin/env python3

import numpy as np


def column_comparison(a):
    # This result will not be a numpy array, also for loops are not necessary
    # result = []
    # b = a[:, ::-1]
    # c = a > b
    # print(c)
    # for i in range(c.shape[0]):
    #     if c[i][1]:
    #         if len(result) == 0:
    #             result = np.array(a[i])
    #         else:
    #             result = np.vstack((result, a[i]))

    # return result

    # This slices 2 columns and compares those, which result in a true/false 1d array (5,)
    b = a[:, 1] > a[:, -2]
    broadcasted_a, broadcasted_b = np.broadcast_arrays(a, b)
    info("broadcasted_a", broadcasted_a)
    info("broadcasted_b", broadcasted_b)

    # This will be used to mask the rows, it is not the same as its broadcasted version
    # Because this would check each element
    # d = [
    #     [True, False, True, True, False],
    #     [True, False, True, True, False],
    #     [True, False, True, True, False],
    #     [True, False, True, True, False],
    #     [True, False, True, True, False],
    # ]
    # return a[d] returns all elements that the condition is true for
    return a[b]


def info(name, a):
    print(
        f"{name} has dim {a.ndim}, shape {a.shape}, size {a.size}, and dtype {a.dtype}:\n {a}"
    )


def main():
    matrix = np.array(
        [
            [8, 9, 3, 8, 8],
            [0, 5, 3, 9, 9],
            [5, 7, 6, 0, 4],
            [7, 8, 1, 6, 2],
            [2, 1, 3, 5, 8],
        ]
    )
    print(column_comparison(matrix))


if __name__ == "__main__":
    main()
