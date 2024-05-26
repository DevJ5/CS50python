#!/usr/bin/env python3


def extract_numbers(s):
    result = []
    list = s.split()
    for item in list:
        try:
            result.append(int(item))
        except:
            try:
                result.append(float(item))
            except:
                pass

    return result


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()
