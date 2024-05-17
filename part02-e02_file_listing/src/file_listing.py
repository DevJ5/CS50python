#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    # drwxr-xr-x 4 jttoivon hyad-all    4096 Nov 29 13:07 _build
    result = []
    with open(filename, "r") as in_file:
        for line in in_file:
            # Simple string split

            # line_list = line.split()
            # hour, minutes = line_list[7].split(":")

            # output = (
            #     int(line_list[4]),
            #     line_list[5],
            #     int(line_list[6]),
            #     int(hour),
            #     int(minutes),
            #     line_list[8],
            # )
            # result.append(output)

            # Complicated regex
            match = re.search(
                r"^.{10}\s+\d+\s+.+\s+(\d+)\s+(\w+)\s+(\d+)\s+(\d\d):(\d\d)\s+(.+)",
                line,
            )

            size, month, day, hour, minute, filename = match.groups()
            result.append(
                (int(size), month, int(day), int(hour), int(minute), filename)
            )

    return result


def main():
    print(file_listing())


if __name__ == "__main__":
    main()
