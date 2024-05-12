#!/usr/bin/env python3


def detect_ranges(L):
    sortedL = sorted(L)
    result = []
    range = None

    print(sortedL)
    for i, number in enumerate(sortedL):
        if i + 1 < len(sortedL) and number + 1 == sortedL[i + 1]:
            if range == None:
                range = (number, sortedL[i + 1] + 1)
            else:
                range = (range[0], sortedL[i + 1] + 1)
        else:
            if range == None:
                range = number
            result.append(range)
            range = None

    return result


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(result)


if __name__ == "__main__":
    main()
