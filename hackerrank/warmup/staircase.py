#!/bin/python3

#https://www.hackerrank.com/challenges/staircase/submissions/code/53369253

import sys


n = int(input().strip())
l = [' '] * n
for i in range(n-1, -1, -1):
    l[i] = '#'
    print(''.join(l))