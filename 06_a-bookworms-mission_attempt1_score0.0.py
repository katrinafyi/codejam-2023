#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    book = []

    for _ in range(n):
        book_item = input()
        book.append(book_item.replace('\\n', '\n').split('\n'))
        for i,x in enumerate(book[-1]):
            book[-1][i] = book[-1][i].split()
    #print(book)
    
    input()
    m = int(input())
    s = [] 
    
    for _ in range(m):
        page, line, i = [int(x) for x in input().split()]
        page -= 1
        line -= 1
        i -= 1
        s.append(book[page][line][i])
        #print(page,line,i)
        #print(s)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(' '.join(s) + '\n')
    fptr.close()
    
