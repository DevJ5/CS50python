#!/usr/bin/env python3


def merge(L1, L2):
    sizeL1 = len(L1)
    sizeL2 = len(L2)

    i = j = 0
    mergedList = []

    while i < sizeL1 and j < sizeL2:
        if L1[i] <= L2[j]:
            mergedList.append(L1[i])
            i += 1
        else:
            mergedList.append(L2[j])
            j += 1

    mergedList = mergedList + L1[i:] + L2[j:]
    return mergedList


def main():
    # Two lists L1 and L2 with ints sorted asc
    L1 = [1, 5, 9, 12]
    L2 = [2, 6, 10]
    mergedList = merge(L1, L2)
    print(mergedList)


if __name__ == "__main__":
    main()
