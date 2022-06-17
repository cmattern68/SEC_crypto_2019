#!/usr/bin/env python3

import sys
import base64
import binascii
import codecs
import os
from Crypto.Cipher import AES

def unpad(s):
    return s[0:-s[-1]]

def getFile(file):
    try:
        if os.stat(file).st_size == 0:
            exit(84)
        with open(file, 'r') as file:
            data = file.readlines()
        return data
    except:
        print('File does not exist')
        exit(84)

def makeAES(file_content):
    content = base64.b64decode(file_content[1])

    key = bytes.fromhex(file_content[0])
    cipher = AES.new(key, AES.MODE_ECB)
    decodeContent = unpad(cipher.decrypt(content))
    reEncodedContent = codecs.encode(decodeContent, 'base64').decode()
    print(reEncodedContent, end='')

def main():
    if len(sys.argv) != 2:
        print("Not enough argument")
        exit(84)
    file_content = getFile(sys.argv[1]);
    makeAES(file_content)

if __name__ == "__main__":
    main()
