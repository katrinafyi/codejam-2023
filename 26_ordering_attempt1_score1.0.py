#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict 

def iterative_topological_sort(graph):
    nodes = set(graph)
    for ns in graph.values():
        nodes.update(ns)
        
    degrees = {x:0 for x in nodes}
    
    # starts = set(nodes)
    for g,ns in graph.items():
        # starts -= ns
        for n in ns: degrees[n] += 1
    # print(nodes)
    # print(starts)
    # print(degrees)
    
    while degrees:
        x = next(d for d in degrees if degrees[d] == 0)
        yield x
        del degrees[x]
        for n in graph[x]:
            degrees[n] -= 1
        
    
def ordering(a):
    
    g = defaultdict(set)
    for x in a:
        for c1,c2 in zip(x,x[1:]):
            g[c1].add(c2)
    print(g)       
        
    # Write your code here
    return ''.join(iterative_topological_sort(g))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nn = int(input().strip())

    xx = []

    for _ in range(nn):
        xx_item = input()
        xx.append(xx_item)

    yy = ordering(xx)

    fptr.write(yy + '\n')

    fptr.close()
