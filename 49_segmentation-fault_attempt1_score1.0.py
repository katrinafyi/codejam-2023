#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'segmentation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY t
#  2. STRING_ARRAY d
#

def get(x):
    x = list(x)
    assert len(x) == 1, str(x)
    return x[0]

def intersect(x):
    x = list(x)
    s = set(x[0])
    for a in x:
        s &= set(a)
    return s

def segmentation(t, d):
    # Write your code here
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tt = []

    for _ in range(10):
        tt_item = input()
        tt.append(tt_item)
        
    # wires = {x: 0 for x in 'tuvwxyz'}    
    
    one = set(get(x for x in tt if len(x) == 2))
    print(one)
    
    seven = set(get(x for x in tt if len(x) == 3))
    
    four = set(get(x for x in tt if len(x) == 4))
    
    TOP = get(seven - one)
    
    MIDDLE_3 = intersect(x for x in tt if len(x) == 5)
    # print(MIDDLE_3)
    MIDDLE_TOP = get(MIDDLE_3 & seven)
    MIDDLE_MID = get(MIDDLE_3 & four)
    MIDDLE_BOT = get(MIDDLE_3 - {MIDDLE_TOP, MIDDLE_MID})
    LEFT_TOP = get(four - {MIDDLE_MID} - one )
    
    five = intersect(x for x in tt if len(set(x) & one) == 1 and len(set(x) & four) == 3)
    
    RIGHT_BOT = get(five & one)
    RIGHT_TOP = get(one - {RIGHT_BOT})
    
    LEFT_BOT = get(set('tuvwxyz') - {MIDDLE_MID, MIDDLE_TOP, MIDDLE_BOT, LEFT_TOP, RIGHT_BOT, RIGHT_TOP})
    
    print(MIDDLE_MID, MIDDLE_TOP, MIDDLE_BOT, LEFT_TOP, RIGHT_BOT, RIGHT_TOP)
    
    """
     0
    5 1
     6
    4 2
     3
    """
    
    shifts = {letter: 1<<pos for pos, letter in enumerate([MIDDLE_TOP, RIGHT_TOP, RIGHT_BOT, MIDDLE_BOT, LEFT_BOT, LEFT_TOP, MIDDLE_MID])}
    print(shifts)
    x0, x1, x2, x3, x4, x5, x6 = [1 << i for i in range(7)]
    
    digits = [
        x0 | x1 | x2 | x3 | x4 | x5,
        x1 | x2,
        x0 | x1 | x6 | x4 | x3,
        x0 | x1 | x2 | x3 | x6, 
        x5 | x6 | x1 | x2, 
        x0 | x5 | x6 | x2 | x3,
        x0 | x5 | x6 | x4 | x2 | x3,
        x0 | x1 | x2, 
        x0 | x1 | x2 | x3 | x4 | x5 | x6,
        x0 | x1 | x5 | x6 | x2 | x3
    ]

    nn = int(input().strip())

    dd = []

    wa = []
    for _ in range(nn):
        dd_item = input()
        d = 0
        for x  in dd_item:
            d |= shifts[x]
        print(dd_item, d)
        wa.append(str(digits.index(d)))
        dd.append(dd_item)

    yy = segmentation(tt, dd)

    fptr.write(''.join(wa) + '\n')

    fptr.close()
