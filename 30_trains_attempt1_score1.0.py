#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'trains' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY m as parameter.
#

forward_slash = {
    (-1,0): (0,1),
    (1,0): (0,-1),
    (0,1): (-1,0),
    (0,-1): (1,0)
}

back_slash = {
    (-1,0): (0,-1),
    (1,0): (0,1),
    (0,1): (1,0),
    (0,-1): (-1,0)
}

def trains(m):
    m = {(x,y): a for x,row in enumerate(m) for y,a in enumerate(row) if a != '.'}
    
    r,c = next(k for k in m if m[k] in ('^$<>'))
    dr,dc = {
        '^': (-1,0),
        '$': (1,0),
        '<': (0,-1),
        '>': (0,1)
    }[m[r,c]]
    
    while m[r,c] != '#':
        
        x = m[r,c]
        # print(r,c,dr,dc,x,x=='/',forward_slash[r,c])
        if x.isalpha():
            yield x
        if x == '/':
            dr,dc = forward_slash[dr,dc]
        elif x == '\\':
            dr,dc = back_slash[dr,dc]
        r += dr
        c += dc         
        # print(r,c,dr,dc)
    

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    mm = []

    for _ in range(nn):
        mm_item = input()
        mm.append(mm_item)

    yy = ''.join(trains(mm))

    fptr.write(yy + '\n')

    fptr.close()
