#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def subfigures(m):
    fig, ax = plt.subplots(1, 2)
    print(ax.shape)
    ax[0].plot(m[:, 0], m[:, 1])
    ax[1].scatter(m[:, 0], m[:, 1], c=m[:, 2], cmap="viridis", s=m[:, 3])
    plt.show()


def main():
    a = np.array([[1, 1, 10, 20], [2, 2, 20, 20], [3, 3, 30, 40], [4, 4, 40, 40]])
    subfigures(a)


if __name__ == "__main__":
    main()
