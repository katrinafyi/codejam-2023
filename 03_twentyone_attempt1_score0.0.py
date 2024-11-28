#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'TwentyOne' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING sequence as parameter.
#

def TwentyOne(sequence):
    s = sequence.split()
    # subtracts one for each 10, jack, queen, king, or ace and 
    # adds one for any card between 2 and 6 (inclusive). 
    # 7s, 8s, and 9s count as zero and do not affect the count.
    x = 0 
    for c in s:
        if c in '10 J Q K A'.split():
            x -= 1
        elif c in '2,3,4,5,6'.split(','):
            x += 1
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inp = input()

    result = TwentyOne(inp)

    fptr.write(str(result) + '\n')

    fptr.close()
