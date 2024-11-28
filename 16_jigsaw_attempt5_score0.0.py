#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jigsaw' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING x as parameter.
#

def jigsaw(x):
    s = x.split()
    from collections import defaultdict 
    chars = defaultdict(lambda: [None,None])
    
    c2 = {}
    
    import re

    r = re.compile(r'(\d+)(.)(\d+)')
    
    for part in s:
        
        m = r.fullmatch(part.strip())
        
        h,x,t = m[1],m[2],m[3]
        h = int(h)
        t = int(t)
        
        chars[h][0] = x
        chars[t][1] = x
        c2[x] = t
    
    front,_ = next(x for x in chars.values() if x[1] is None)
    
    
    x = front 
    s = ''
    while x is not None:
        # print(x)
        s += x
        x = chars[c2[x]][0]
        # s +=
    # print('--')
    # print(chars)
    # print(c2)
    return s
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    xx = input()

    yy = jigsaw(xx)

    fptr.write(yy + '\n')

    fptr.close()
