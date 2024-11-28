#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'castles' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts following parameters:
#  1. STRING_ARRAY a
#  2. INTEGER_ARRAY s
#

def castles(a, s):
    from collections import defaultdict
    archs = defaultdict(list)
    for arch, score in zip(a,s):
        for a in arch:
            archs[a] .append(score)
    
    l = max(len(x) for x in archs.values())
    for a in archs:
        if len(archs[a]) < l:
            archs[a] = archs[a] + [None] * (l - len(archs[a]))
        archs[a].sort()
                    
    # print(archs)
    return max(archs, key=archs.get)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    aa = input().rstrip().split()

    ss = list(map(int, input().rstrip().split()))

    yy = castles(aa, ss)

    fptr.write(str(yy) + '\n')

    fptr.close()
