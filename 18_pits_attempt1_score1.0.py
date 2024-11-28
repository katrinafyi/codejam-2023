#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def pits(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    
    def get(r,c):
        if not 0 <= r < rows:
            return float('inf')
        if not 0 <= c < cols:
            return float('inf')
        return grid[r][c]

    n = 0
    for r in range(rows):
        for c in range(cols):
            x = grid[r][c]
            if all(x < get(r2,c2) for r2,c2 in [[r,c+1],[r,c-1],[r+1,c],[r-1,c]]):
                n += 1
    return n
                
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    mm = int(first_multiple_input[0])

    nn = int(first_multiple_input[1])

    gg = []

    for _ in range(mm):
        gg.append(list(map(int, input().rstrip().split())))

    yy = pits(gg)

    fptr.write(str(yy) + '\n')

    fptr.close()
