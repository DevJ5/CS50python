#!/usr/bin/env python3

import numpy as np


def multiplication_table(n):
    result = []
    a = np.arange(0, n)
    b = a.reshape(n, 1)
    result = a * b

    broadcasted_a, broadcasted_b = np.broadcast_arrays(a, b)
    info("broadcasted_a", broadcasted_a)
    info("broadcasted_b", broadcasted_b)
    return result


def info(name, a):
    print(
        f"{name} has dim {a.ndim}, shape {a.shape}, size {a.size}, and dtype {a.dtype}:\n {a}"
    )


def main():
    print(multiplication_table(4))


if __name__ == "__main__":
    main()
