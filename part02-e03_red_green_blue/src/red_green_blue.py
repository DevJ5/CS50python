#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    #     ! $Xorg: rgb.txt,v 1.3 2000/08/17 19:54:00 cpqbld Exp $
    # 255 250 250		snow

    result = []
    with open(filename, "r") as in_file:
        next(in_file)
        for line in in_file:
            match = re.match(
                r"\s*(\d{0,3})\s+(\d{0,3})\s+(\d{0,3})\s+(\w+|\w+\s\w+|\w+\s\w+\s\w+)$",
                line,
            )
            result.append("\t".join(match.groups()))

    print(result)
    return result


def main():
    red_green_blue()


if __name__ == "__main__":
    main()
