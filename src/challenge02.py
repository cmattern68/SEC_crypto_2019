#!/usr/bin/env python3

import sys
import os

def fileLen(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getFile(file):
    try:
        if os.stat(file).st_size == 0:
            exit(84)
        if (fileLen(file) == 2):
            with open(file, 'r') as file:
                data = file.read()
            array = data.split('\n')
            return array
        else:
            print("Too much line")
            exit(84)
    except:
        print('File does not exist')
        exit(84)

def main():
    try:
        if len(sys.argv) != 2:
            print("Not enough argument")
            exit(84)
        file_content = getFile(sys.argv[1])
        if (len(file_content[0]) != len(file_content[1])):
            print('The two string has not the same length.')
            exit(84)
        value = (hex(int(file_content[0], 16) ^ int(file_content[1], 16))).lstrip("0x")
        print(value.upper())
    except ValueError:
        exit(84)

if __name__ == "__main__":
    main()
