#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abundant_numbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY sequence
#

def get_divisors(n):
    """
    :param n: positive integer.
    :return: list of all different divisors of n.
    """
    if n <= 0:
        return []
    divisors = [1, n]
    for div in range(1, int(n ** 0.5 + 1)):
        if n % div == 0:
            divisors.extend([n // div, div])
    return sorted(list(set(divisors) - {n}))

def abundant_numbers(n, sequence):
    for x in sequence:
        divs = sum(get_divisors(x))
        if divs > x:
            yield x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    qq = list(map(int, input().rstrip().split()))

    result = abundant_numbers(nn, qq)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
