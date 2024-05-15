#!/usr/bin/env python3


def interleave(*lists):
    zippedLists = list(zip(*lists))

    # Faster way
    return list(sum(zippedLists, ()))

    # result = []
    # for l in zippedLists:
    #     for i in l:
    #         result.extend([i])
    # return result


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ["a", "b", "c"]))


if __name__ == "__main__":
    main()
