#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
##
## File description:
##
##

import sys

def xor(str, key):
    xor = b''
    i = 0
    for b in range (len(str)):
        xor += bytes([key[i] ^ str[b]])
        if (i + 1) == len(key):
            i = 0
        else:
            i += 1
    return xor

def parse():
    if len(sys.argv) != 2:
        exit(84)
    else:
        try:
            f = open(sys.argv[1], "r")
            key = f.readline()
            str = f.read()
            key = key.replace('\n', '')
            str = str.replace('\n', '')
            if (str == ""):
                exit(84)
            cyphertex = xor(bytes.fromhex(str), bytes.fromhex(key))
            print(cyphertex.hex().upper())
        except:
            exit(84)

def main():
    parse()

if __name__ == "__main__":
    main()
