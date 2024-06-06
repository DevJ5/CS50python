#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a):
    return tuple(
        (i / 2 - 0.5 for i in a.shape[0:2])
    )  # note the order: (center_y, center_x)


def radial_distance(a):
    rows, columns = a.shape[0:2]
    c = center(a)
    dist_array = np.zeros((rows, columns))
    for (i, j), element in np.ndenumerate(dist_array):
        dist_array[i][j] = np.linalg.norm(np.array((i, j)) - np.array(c))

    return dist_array


def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax]."""
    return np.interp(a, (a.min(), a.max()), (tmin, tmax))


def radial_mask(a):
    return scale(1 - radial_distance(a))


def radial_fade(a):
    height, width = a.shape[0:2]
    mask = radial_mask(a).reshape(height, width, 1)
    ret = a * mask
    return ret


def main():
    painting = plt.imread("src/painting.png")
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(painting)
    ax[1].imshow(radial_mask(painting))
    ax[2].imshow(radial_fade(painting))
    plt.show()

    print(radial_fade(np.zeros((10, 11, 3))))


if __name__ == "__main__":
    main()
