#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'ocr' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY s as parameter.
#

chars = '''.AAA.
A...A
AAAAA
A...A
A...A

BBBB.
B...B
BBBB.
B...B
BBBB.

.CCCC
C....
C....
C....
.CCCC

DDDD.
D...D
D...D
D...D
DDDD.

.EEEE
E....
EEEEE
E....
.EEEE

.FFFF
F....
FFFFF
F....
F....

.GGGG
G....
G.GGG
G...G
.GGGG

H...H
H...H
HHHHH
H...H
H...H

IIIII
..I..
..I..
..I..
IIIII

..JJJ
....J
....J
J...J
.JJJ.

K...K
K..K.
KKK..
K..K.
K...K

L....
L....
L....
L....
LLLLL

.M.M.
M.M.M
M.M.M
M.M.M
M.M.M

N...N
NN..N
N.N.N
N..NN
N...N

.OOO.
O...O
O...O
O...O
.OOO.

PPPP.
P...P
PPPP.
P....
P....

.QQQ.
Q...Q
Q...Q
Q..Q.
.QQ.Q

RRRR.
R...R
RRRR.
R.R..
R..RR

.SSSS
S....
.SSS.
....S
SSSS.

TTTTT
..T..
..T..
..T..
..T..

U...U
U...U
U...U
U...U
.UUU.

V...V
V...V
V...V
.V.V.
..V..

W.W.W
W.W.W
W.W.W
W.W.W
.W.W.

X...X
.X.X.
..X..
.X.X.
X...X

Y...Y
Y...Y
.Y.Y.
..Y..
..Y..

ZZZZZ
...Z.
..Z..
.Z...
ZZZZZ'''.split('\n\n')

for i,x in enumerate(chars):
    x = x.strip().split()
    ss = set()
    for r,row in enumerate(x):
        for c,aa in enumerate(row):
            if aa != '.':
                ss.add((r,c))
    chars[i] = ss
    # print(len(ss))
    
# print(chars)
# print(len(chars))

def ocr(s):
    from pprint import pprint 
    # pprint(s)
    # Write your code here
    cc = 0
    
    while cc+5 <= len(s[0]):
        found = False
        for i,pattern in enumerate(chars):
            r,c= next(iter(pattern))
            
            key = s[r][cc + c]
            
            if all(s[r][cc+c] == key for r,c in pattern):
                yield chr(ord('A') + i)
                found = True
                break
                
        if found:
            cc += 5        
        else:
            cc += 1
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    xx = []

    for _ in range(5):
        xx_item = input()
        xx.append(xx_item)

    yy = ''.join(ocr(xx))

    fptr.write(yy + '\n')

    fptr.close()
