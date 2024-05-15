#!/usr/bin/env python3


def main():
    result = [(x, y) for x in range(1, 7) for y in range(1, 7) if x + y == 5]

    for pair in result:
        print(pair)


if __name__ == "__main__":
    main()
