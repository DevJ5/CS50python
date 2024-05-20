#!/usr/bin/env python3

import sys
import math


def summary(filename):
    with open(filename, "r") as in_file:
        sum = 0
        count = 0
        numbers = []
        for line in in_file:
            try:
                numbers.append(float(line))
            except ValueError:
                print(
                    "The file contains strings, which have been ignored by the calculation!"
                )

        if len(numbers) == 0:
            return (0, 0, 0)

        for number in numbers:
            sum += number
            count += 1

        average = sum / count

        sumSquaredDeviations = 0

        for number in numbers:
            squaredDeviation = pow(number - average, 2)
            sumSquaredDeviations += squaredDeviation

        stdv = math.sqrt(sumSquaredDeviations / (len(numbers) - 1))

        return (sum, average, stdv)


def main():
    files = sys.argv[1:]
    for file in files:
        sum, average, stdv = summary(file)
        print(f"File: {file} Sum: {sum:.6f} Average: {average:.6f} Stddev: {stdv:.6f}")


if __name__ == "__main__":
    main()
