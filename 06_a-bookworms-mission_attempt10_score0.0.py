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
            book[-1][i] = book[-1][i].strip().split()
    #print(book)
    
    prev = input().strip()
    is_test = prev
    m = int(prev if prev else input())
    s = [] 
    
    for _ in range(m):
        page, line, i = [int(x) for x in input().split()]
        if is_test:
            page -= 1
            line -= 1
            i -= 1
        s.append(book[page][line][i].strip())
        #print(page,line,i)
        #print(s)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(' '.join(s) + '\n')
    fptr.close()
    
