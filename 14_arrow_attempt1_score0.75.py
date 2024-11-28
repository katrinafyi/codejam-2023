#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrow' function below.
#
# The function is expected to return a FLOAT_ARRAY.
# The function accepts following parameters:
#  1. DOUBLE x
#  2. DOUBLE y
#  3. DOUBLE u
#  4. DOUBLE g
#

def arrow(x, y, u, g):
    from math import sqrt, degrees,atan,cos
    b = x
    a = y
    x1 = (b* u**2 - sqrt(-b**2* (2 *a* g* u**2 + b**2* g**2 - u**4)))/(b**2 *g)
    
    x2 = (sqrt(-b**2 *(2 *a *g* u**2 + b**2 *g**2 - u**4)) + b* u**2)/(b**2* g)
    # Write your code here
    print(x1,x2)
    t = atan(x1)
    t2 = atan(x2)
    d1 = degrees(t)
    d2 = degrees(t2)
    
    time1 = x / (u * cos(t))
    time2 = x / (u * cos(t2))
    
    if time1 < time2:
        yield from [d1, time1, d2, time2]
    else:
        yield from [d2, time2,d1, time1]
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    xx = float(first_multiple_input[0])

    yy = float(first_multiple_input[1])

    uu = float(first_multiple_input[2])

    gg = float(first_multiple_input[3])

    aa = arrow(xx, yy, uu, gg)

    fptr.write('\n'.join(map(str, aa)))
    fptr.write('\n')

    fptr.close()
