#!/usr/bin/python3
def uppercase(c):
    for ch in c:
        if ord(ch) >= 97 or ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
        print("{:s}".format(ch), end='')
    print('\n', end='')
