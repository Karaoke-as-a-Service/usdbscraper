#!/usr/bin/env python3.6

import sys
import argparse


def set_attr(content, value, attr):
    found = False
    for line in content:
        if line.startswith(f'#{attr}:'.encode()):
            found = True
            yield f'#{attr}:{value}\n'.encode()
        else:
            if not found and not line.startswith('#'.encode()):
                found = True
                yield f'#{attr}:{value}\n'.encode()
            yield line


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('attribute')
    parser.add_argument('value')
    args = parser.parse_args()

    for file in sys.stdin.readlines():
        file = file.strip()

        if not file:
            continue

        print(file)

        with open(file, 'rb') as f:
            content = list(f.readlines())
        content = list(set_attr(content, args.value, args.attribute))

        with open(file, 'wb') as f:
            f.writelines(content)



if __name__ == '__main__':
    main()
