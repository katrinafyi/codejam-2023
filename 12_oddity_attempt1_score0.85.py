#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'oddity' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY a as parameter.
#

def oddity(a):
    from collections import defaultdict
    chars = defaultdict(int)
    for s in a:
        
        for c in set(s):
            chars[c] += 1
        
    print(chars)
    for c in sorted(chars):
        if chars[c] % 2 == 1: 
            yield c
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    aa = []

    for _ in range(nn):
        aa_item = input()
        aa.append(aa_item)

    yy = oddity(aa)

    fptr.write(''.join(yy) + '\n')

    fptr.close()
