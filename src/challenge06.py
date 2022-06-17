#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
##
## File description:
##
##

import sys
import binascii
import codecs

frequency = {
    'A': 8.167, 'B': 1.492, 'C': 2.782, 'D': 4.253,
    'E': 12.702, 'F': 2.228, 'G': 2.015, 'H': 6.094,
    'I': 6.094, 'J': 0.153, 'K': 0.772, 'L': 4.025,
    'M': 2.406, 'N': 6.749, 'O': 7.507, 'P': 1.929,
    'Q': 0.95, 'R': 5.987, 'S': 6.327, 'T': 9.056,
    'U': 2.758, 'V': 0.978, 'W': 2.360, 'X': 0.150,
    'Y': 1.974, 'Z': 0.074, ' ': 13.000
}

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

def hamming_distance(s1, s2):
    sum = 0
    if len(s1) != len(s2):
        raise 84
    for i in range (0, len(s1), 1):
        bin1 = bin(s1[i])
        bin2 = bin(s2[i])
        bin1 = bin1[2:]
        bin2 = bin2[2:]
        if (len(bin1) < 8):
            bin1 = bin1.zfill(8)
        if (len(bin2) < 8):
            bin2 = bin2.zfill(8)
        for a in range (0, len(bin1)):
            if (bin1[a] != bin2[a]):
                sum += 1
    return sum

def parse():
    if len(sys.argv) != 2:
        exit(84)
    else:
        try:
            f = open(sys.argv[1], "r")
            str = f.read()
            str = str.replace('\n', '')
            if (str == ""):
                exit(84)
            str = bytes.fromhex(str)
            average_distances = []
            for keysize in range (5, 41):
                blocks = [str[i:i+keysize] for i in range (0, len(str), keysize)]
                block1 = blocks[0]
                block2 = blocks[1]
                distance = hamming_distance(block1, block2)
                del blocks[0]
                del blocks[1]
                result = {'keysize': keysize,'distance': distance / keysize}
                average_distances.append(result)
            average_distances = sorted(average_distances, key=lambda x: x['distance'])
            keysize = average_distances[0]['keysize']
            blocks = [str[i:i+keysize] for i in range (0, len(str), keysize)]
            blocks2 = []
            result = b''
            for i in range (0, keysize):
                teub = b''
                for a in range (i, len(str), keysize):
                    teub += bytes([str[a]])
                blocks2.append(teub)
            for i in range(0, int(len(blocks2) / 2)):
                result = xorAllBytesForResult(blocks2[i])
                print(result.upper(), end='')
        except:
            raise
            exit(84)

def main():
    parse()

if __name__ == "__main__":
    main()
