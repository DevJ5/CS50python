"""Module containing functions calculating triangle properties"""

__version__ = "1.0"
__author__ = "DevJ5"

import math


def hypotenuse(a, b):
    # a^2 + b^2 = c^2
    """Returns the hypoteuse of right angled triangle when given lengths of two other sides"""
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))


def area(a, b):
    """Returns the area of the right-angled triangle, when two sides, perpendicular to each other, are given as parameters."""
    return float(a * b) / 2
