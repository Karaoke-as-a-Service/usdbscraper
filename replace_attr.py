#!/usr/bin/env python3.6

import sys
from ultrastartxt import get_attr, set_attr
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hide-filename', action='store_true', default=False)
    parser.add_argument('--dry-run', action='store_true', default=False)
    parser.add_argument('attribute')
    parser.add_argument('old')
    parser.add_argument('new')
    args = parser.parse_args()

    for file in sys.stdin.readlines():
        file = file.strip()
        content = list(open(file).readlines())

        try:
            value = get_attr(content, args.attribute).strip()
        except:
            value = None

        if value == args.old:
            content = set_attr(content, args.new, args.attribute)

            if not args.dry_run:
                with open(file, 'w') as f:
                    f.writelines(content)

            if not args.hide_filename:
                print(file)


if __name__ == '__main__':
    main()
