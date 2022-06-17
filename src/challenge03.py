#!/usr/bin/env python3

import sys
import os
import binascii

frequency = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253,
    'E': 12.702, 'F': 2.228, 'G': 2.015, 'H': 6.094,
    'I': 6.094, 'J': 0.153, 'K': 0.772, 'L': 4.025,
    'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929,
    'Q': 0.95, 'R': 5.987, 'S': 6.327, 'T': 9.056,
    'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
    'Y': 1.974, 'Z': 0.074, ' ': 13.000
}

def fileLen(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def getFile(file):
    try:
        if os.stat(file).st_size == 0:
            exit(84)
        if (fileLen(file) == 1):
            with open(file, 'r') as file:
                data = file.read()
            return data
        else:
            exit(84)
    except:
        print('File does not exist')
        exit(84)

def englishScore(str):
    str = str.upper()
    score = 0.0
    for char in str:
        if char in frequency:
            score += frequency[char]
    return score

def getResult(scoreArray, finalArray):
    bestScore = 0.0
    for score in scoreArray:
        if score > bestScore:
            bestScore = score
    if not finalArray:
        return None
    return finalArray[bestScore]


def xorAllBytesForResult(str):
    scoreArray = []
    finalArray = {}
    for xor in range(0, 256):
        try:
            decodeStr = b''
            for char in str:
                decodeStr += bytes([char ^ xor])
            finalStr = decodeStr.decode("utf-8")
            score = englishScore(finalStr)
            scoreArray.append(score)
            finalArray[score] = hex(xor).lstrip("0x")
        except:
            continue
    return getResult(scoreArray, finalArray)

def main():
    try:
        if len(sys.argv) != 2:
            print("Not enough argument")
            exit(84)
        file = getFile(sys.argv[1])
        fileHex = int(file, 16)
        file_content = bytearray.fromhex(file)
        result = xorAllBytesForResult(file_content)
        print(result)
    except ValueError:
        exit(84)

if __name__ == "__main__":
    main()
