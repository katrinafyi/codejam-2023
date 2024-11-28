#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'MiningCS' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING directions as parameter.
#

m = {
    'r': 'right',
    'l': 'left',
    's': 'straight',
    'j': 'jump'
}

def MiningCS(directions):
    o = ''
    for c in directions:
        o += m.get(c.lower(), 'Aaaaah!') + '\n'
    return o.strip()
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inp = input()

    result = MiningCS(inp)

    fptr.write(result + '\n')

    fptr.close()
