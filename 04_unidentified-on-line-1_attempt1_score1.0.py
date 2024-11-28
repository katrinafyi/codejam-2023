#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'test_if_braces_match' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING braces as parameter.
#

def test_if_braces_match(braces):
    d = 0
    for c in braces:
        if c == '{':
            d += 1
        elif c == '}':
            if d == 0:
                return 0
            d -= 1
    return 1 if d == 0 else 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    braces = input()

    do_braces_match = test_if_braces_match(braces)

    fptr.write(str(do_braces_match) + '\n')

    fptr.close()
