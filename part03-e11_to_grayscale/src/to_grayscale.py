#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(img):
    w_red = 0.2126
    w_green = 0.7152
    w_blue = 0.0722
    w_vector = np.array([w_red, w_green, w_blue])

    return img @ w_vector


def to_red(img):
    return img * np.array([1, 0, 0])


def to_green(img):
    return img * np.array([0, 1, 0])


def to_blue(img):
    return img * np.array([0, 0, 1])


def main():
    painting = plt.imread("src/painting.png")

    greyscaled = to_grayscale(painting)
    plt.imshow(greyscaled)
    plt.gray()
    plt.show()

    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(to_red(painting))
    ax[1].imshow(to_green(painting))
    ax[2].imshow(to_blue(painting))
    plt.set_cmap("viridis")
    plt.show()


# def info(name, a):
#     print(
#         f"{name} has dim {a.ndim}, shape {a.shape}, size {a.size}, and dtype {a.dtype}:\n {a}"
#     )

# a = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# b = np.array([10, 20, 30])
# print(np.dot(a, b))

# broadcasted_a, broadcasted_b = np.broadcast_arrays(a, b)
# info("broadcasted_a", broadcasted_a)
# info("broadcasted_b", broadcasted_b)


if __name__ == "__main__":
    main()
