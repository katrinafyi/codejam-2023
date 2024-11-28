#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'tile' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts 2D_INTEGER_ARRAY a as parameter.
#

def tile(a):
    placed = set()
    score = 0
    for x,y in a:
        x0,y0 = x,y
        s = 0
        
        dx,dy = 1,0
        while (x+dx,y+dy) in placed:
            s += 1
            x += dx
            y += dy
        x,y = x0,y0
        
        dx,dy = -1,0
        while (x+dx,y+dy) in placed:
            s += 1
            x += dx
            y += dy
        x,y = x0,y0
        
        if s: s += 1
        
        
        s0 = s
        dx,dy = 0,1
        while (x+dx,y+dy) in placed:
            s += 1
            x += dx
            y += dy
        x,y = x0,y0
        
        dx,dy = 0,-1
        while (x+dx,y+dy) in placed:
            s += 1
            x += dx
            y += dy
        x,y = x0,y0
        
        if s > s0: s += 1
            
        if s == 0: s += 1
        
        
        
        score += s
        placed.add((x,y))
        
    return (score)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tt = int(input().strip())

    aa = []

    for _ in range(tt):
        aa.append(list(map(int, input().rstrip().split())))

    yy = tile(aa)

    fptr.write(str(yy) + '\n')

    fptr.close()
