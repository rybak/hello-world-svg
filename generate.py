#!/usr/bin/env python3

digits = []

for c in 'Hello, world!':
    digits.append('{0:08b}'.format(ord(c)))

for d in digits:
    print(d)

