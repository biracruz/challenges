#!/bin/python3
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D=warmup
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/submissions/code/130339687?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup&isFullScreen=true
import math
import os
import random
import re
import sys


def two_consecutives(arr, new_e):
    if arr[-2] + 1 == arr[-1] and arr[-1] + 1 == new_e:
        return True
    else:
        return False

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = list()
    for i, actual in enumerate(c): 
        if actual == 0:                        
            if len(jumps) > 1 and two_consecutives(jumps, i):                
                jumps.pop()
            jumps.append(i)
    return len(jumps)-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()