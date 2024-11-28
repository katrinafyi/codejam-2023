#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'is_there_apple' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING message as parameter.
#

def is_there_apple(message):
    i = 0 
    c = 'a'
    found = False
    while i < len(message):
        if message[i].lower() == c:
            found = True 
            break
        i += 1
    i += 1
    if not found:
        return ''
    c = 'p'
    found = False
    while i < len(message):
        if message[i].lower() == c:
            found = True 
            break
        i += 1
    i += 1
    if not found:
        return ''
    c = 'p'
    found = False
    while i < len(message):
        if message[i].lower() == c:
            found = True 
            break
        i += 1
    i += 1
    if not found:
        return ''
    c = 'l'
    found = False
    while i < len(message):
        if message[i].lower() == c:
            found = True 
            break
        i += 1
    i += 1
    if not found:
        return ''
    c = 'e'
    found = False
    while i < len(message):
        if message[i].lower() == c:
            found = True 
            break
        i += 1
    i += 1
    if not found:
        return ''
    return 'apple that I am going to eat'
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    message = input()

    reply = is_there_apple(message)

    fptr.write(reply + '\n')

    fptr.close()
