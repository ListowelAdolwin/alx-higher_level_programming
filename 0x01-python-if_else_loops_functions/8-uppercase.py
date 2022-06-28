#!/usr/bin/python3

def uppercase(str):
    result = ''
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            result += chr(ord(letter) - 32)
        else:
            result += letter
    print("{:s}".format(result))
