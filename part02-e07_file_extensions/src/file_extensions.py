#!/usr/bin/env python3


def file_extensions(filename):
    list = []
    dict = {}

    with open(filename, "r") as in_file:
        for line in in_file:
            line = line.rstrip("\n")
            if "." not in line:
                list.append(line)
            else:
                fileExtension = line.split(".")[-1]
                try:
                    dict[fileExtension].append(line)
                except:
                    dict[fileExtension] = [line]

    return (list, dict)


def main():
    list, dict = file_extensions("src/filenames.txt")
    print(f"{len(list)} files with no extension")
    for key in dict:
        print(f"{key} {len(dict[key])}")


if __name__ == "__main__":
    main()
