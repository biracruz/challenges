#!/bin/python3

#https://www.hackerrank.com/challenges/mini-max-sum/submissions/code/53371612

import sys

arr = list(map(int, input().strip().split(' ')))
_arr = sorted(arr)
print(str(sum(_arr[:4]))+' '+str(sum(_arr[1:5])))