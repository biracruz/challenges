#!/bin/python3
# https://www.hackerrank.com/challenges/diagonal-difference/submissions/code/53312378

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

s1 = 0
s2 = 0
for i in range(n):
    s1 = s1 + a[i][i]
    s2 = s2 + a[n-i-1][i]
    
print(abs(s1-s2))