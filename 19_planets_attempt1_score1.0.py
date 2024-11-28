#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'planets' function below.
#
# The function is expected to return a FLOAT_ARRAY.
# The function accepts 2D_INTEGER_ARRAY p as parameter.
#

def planets(planets):
    
    income = [0] * len(planets[0])
    nres = len(income)
    
    for planet in planets:
        m = max(planet)
        
        nz = 0
        # equal = [res for res in planet if res == m]
        for i in range(nres):
            if planet[i] < m:
                planet[i] = 0
            else:
                nz += 1
        for i in range(nres):
            income[i] += planet[i] / nz
    return income
                
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    nn = int(first_multiple_input[0])

    mm = int(first_multiple_input[1])

    pp = []

    for _ in range(nn):
        pp.append(list(map(int, input().rstrip().split())))

    yy = planets(pp)

    fptr.write('\n'.join(map(str, yy)))
    fptr.write('\n')

    fptr.close()
