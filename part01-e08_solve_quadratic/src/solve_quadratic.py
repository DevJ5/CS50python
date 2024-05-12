#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    # ax^2 + bx + c
    discriminant = math.sqrt(b**2 - 4 * a * c)
    if discriminant < 0:
        print("Complex number")
    elif discriminant == 0:
        root1 = -b / (2 * a)
        return (root1, root1)
    else:
        root1 = (-b + discriminant) / (2 * a)
        root2 = (-b - discriminant) / (2 * a)
        return (root1, root2)


def main():
    print(solve_quadratic(1, -3, 2))
    print(solve_quadratic(1, 2, 1))


if __name__ == "__main__":
    main()
