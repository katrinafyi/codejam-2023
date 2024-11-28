#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Mocking' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY d
#  3. STRING m
#

def Mocking(n, d, m):
    s = ''
    for x,c in enumerate(m):
        if any(x % dd == 0 for dd in d):
            if c == c.upper():
                s += c.lower()
            else:
                s += c.upper()
        else:
            s += c
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    k = int(input().strip())

    aa = list(map(int, input().rstrip().split()))

    s = input()

    result = Mocking(k, aa, s)

    fptr.write(result + '\n')

    fptr.close()
