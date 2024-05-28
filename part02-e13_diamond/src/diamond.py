#!/usr/bin/env python3

import numpy as np


def diamond(n):
    upper_half_part_1 = np.eye(n, dtype=int)[::-1]
    upper_half_part_2 = np.eye(n, dtype=int)[:, 1:]
    upper_half = np.concatenate((upper_half_part_1, upper_half_part_2), axis=1)

    lower_half_part_1 = np.eye(n, dtype=int)[1:]
    lower_half_part_2 = np.eye(n, dtype=int)[::-1][1:, 1:]
    lower_half = np.concatenate((lower_half_part_1, lower_half_part_2), axis=1)

    diamond = np.concatenate((upper_half, lower_half), axis=0)

    return diamond


def main():
    diamond(3)


if __name__ == "__main__":
    main()
