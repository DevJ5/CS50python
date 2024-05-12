#!/usr/bin/env python3

import math


def main():
    # Area of triangle, rectangle, circle
    SHAPE_TRIANGLE = "triangle"
    SHAPE_RECTANGLE = "rectangle"
    SHAPE_CIRCLE = "circle"

    area = 0

    while True:
        iShape = input(
            f"Choose a shape ({SHAPE_TRIANGLE}, {SHAPE_RECTANGLE}, {SHAPE_CIRCLE}): "
        )
        if iShape == "":
            break
        if iShape == SHAPE_TRIANGLE:
            iBase = int(input("Give base of the triangle: "))
            iHeight = int(input("Give height of the triangle: "))
            area = iBase * iHeight / 2
        elif iShape == SHAPE_RECTANGLE:
            iBase = int(input("Give base of the triangle: "))
            iHeight = int(input("Give height of the triangle: "))
            area = iBase * iHeight
        elif iShape == SHAPE_CIRCLE:
            iRadius = int(input("Give radius of the circle: "))
            area = iRadius**2 * math.pi
        else:
            print("Unknown shape!")
            continue
        print(f"The area is {area:.4f}")


if __name__ == "__main__":
    main()
