#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truth' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING x as parameter.
#

def truth(x):
    vars = x.replace('(','').replace(')','').replace('~','').replace('&','').replace('|','').replace('0', '').replace('1', '').replace('^','').replace(' ','')
    
    vars = list(sorted(set(vars)))
    print(vars)
    
    x = x.replace('&', ' and ').replace('|', ' or ').replace('^', ' ^ ').replace('1', ' 1 ').replace('0', ' 0 ').replace('~', ' 1 - ').replace('(', 'int(')
    print(x)
    from itertools import product 
    
    
    out = []
    aa = ' '.join(vars)+ ' | ='
    out .append(aa)
    out.append('-'*(len(aa)-3) + '+--')
          
    for bits in product([0,1], repeat=len(vars)):
        bits = list(bits)
        print(bits)
        ls = {v: int(b) for v,b in zip(vars, bits)}
        print(ls)
        
        s = ' '.join(str(x) for x in bits) + ' | '
        s += str(int(bool(eval(x, None,ls))))
        out.append(s)
        
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    xx = input()

    yy = truth(xx)

    fptr.write('\n'.join(yy))
    fptr.write('\n')

    fptr.close()
