#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'graph' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY c
#  2. STRING_ARRAY d
#

import math
def myround(x, base=5):
    return base * math.ceil(x/base)

def graph(c, d):
    counts = c
    len_food = max(len(x) for x in d)
    len_plot = max(myround(n) for n in c)
    
    len_number = len(str(len_plot))
    
    g = [[' ']*(len_number + 2 + 2*len(d)) for _ in range(len_food + len_plot + 1)]
    
    for i in range(len_plot):
        g[i][len_number + 1] = '|'
    for i in range(0, len_plot+1, 5):
        g[i][len_number] = '-'
        s = str(len_plot - i).rjust(len_number)
        for ci, c in enumerate(s):
            g[i][ci] = c
    for j in range(len_number, len(g[0])-1,2):
        g[len_plot][j] = '-'
        g[len_plot][j+1] = '+'
    
    for n,food in enumerate(d):
        for i,c in enumerate(food):
            g[len_plot+1+i][2*n + len_number+2 + 1] = c
            
        for i in range(counts[n]):
            g[len_plot-1-i][2*n + len_number+2 + 1] = '#'
        
    from pprint import pprint 
    
    if len_number > max(len(x) for x in c) + 1:
        g = g[len_number - (max(len(x) for x in c)+1):]
    
    # pprint(g)
    
    return ((''.join(x) for x in g))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    cc = list(map(int, input().rstrip().split()))

    dd = input().rstrip().split()

    yy = graph(cc, dd)

    fptr.write('\n'.join(yy))
    fptr.write('\n')

    fptr.close()
