#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'joel' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY a as parameter.
#

def joel(a):
    import re
    
    a2 = [] 
    for x in a:
        old = x
        x = x[::-1]
        m = re.search(r'(\d+-?)', x)
        n = int(m[1][::-1])
        a2.append((n,old))
        
    a2.sort()
    return [x[1] for x in a2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    aa = []

    for _ in range(nn):
        aa_item = input()
        aa.append(aa_item)

    yy = joel(aa)

    fptr.write('\n'.join(yy))
    fptr.write('\n')

    fptr.close()
