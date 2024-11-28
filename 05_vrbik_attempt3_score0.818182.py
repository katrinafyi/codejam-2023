#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'Vrbik' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY arr
#

def Vrbik(n, arr):
    a = []
    for n, min, max in arr:
        if min <= n <= max:
            a.append(n)
        else:
            a.append(-1)
    if a and all(x == -1 for x in a):
        return []
    return a
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip().split()[0])

    ll = []

    for _ in range(nn):
        ll.append(list(map(int, input().rstrip().split())))

    result = Vrbik(nn, ll)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
