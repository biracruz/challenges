#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    _max = 0
    count = 0
    for h in ar:
        if h > _max:
            _max = h
            count = 1
        else:
            if h == _max:
                count = count + 1
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)