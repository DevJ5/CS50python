#!/usr/bin/env python3
def triple(n):
    return n * 3


def square(n):
    return n**2


def main():

    for i in range(1, 11):
        iTripled = triple(i)
        iSquared = square(i)
        if iSquared > iTripled:
            break
        print(f"triple({i})=={iTripled}", f"square({i})=={iSquared}")


if __name__ == "__main__":
    main()
