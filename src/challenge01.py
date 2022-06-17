#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
##
## File description:
##
##

import sys
from binascii import b2a_base64
import codecs

def parse():
    if len(sys.argv) != 2:
        exit(84)
    else:
        try:
            f = open(sys.argv[1], "r")
            length = len(f.read()) - 1
            if (length % 2) != 0:
                exit(84)
            f = open(sys.argv[1], "r")
            str = f.read(length)
            b64 = codecs.encode(codecs.decode(str, 'hex'), 'base64').decode()
            b64 = b64.replace('\n', '')
            print(b64, end='')
        except:
            exit(84)

def main():
    parse()


if __name__ == "__main__":
    main()
