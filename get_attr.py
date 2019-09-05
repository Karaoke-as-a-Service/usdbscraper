#!/usr/bin/env python3.6

import sys
from ultrastartxt import get_attr
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hide-filename', action='store_true')
    parser.add_argument('attribute')
    args = parser.parse_args()

    for file in sys.stdin.readlines():
        file = file.strip()

        try:
            value = get_attr(open(file).readlines(), args.attribute).strip()
        except:
            continue

        print(value, end='')

        if not args.hide_filename:
            print(' ' + file, end='')

        print()


if __name__ == '__main__':
    main()
