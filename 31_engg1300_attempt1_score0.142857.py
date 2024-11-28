#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l 
#  2. INTEGER_ARRAY a array
#  3. INTEGER n number connected
#  4. INTEGER k target resistance
#

def solution(l, a, n, k):
    # Write your code here
    
    from itertools import combinations
    best = None
    for comb in combinations(a, n):
        if 1/sum(1/x for x in comb) >= k:
            if not best or max(best) > max(comb):
                best = comb 
    if best is None: return [-1]
    return list(sorted(best))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ll = int(input().strip())

    aa = list(map(int, input().rstrip().split()))

    nn = int(input().strip())

    kk = int(input().strip())

    r = solution(ll, aa, nn, kk)

    fptr.write(' '.join(map(str, r)))
    fptr.write('\n')

    fptr.close()
