#!/bin/python3
# https://www.hackerrank.com/challenges/sock-merchant/problem
# https://www.hackerrank.com/challenges/sock-merchant/submissions/code/130336012

import math
import os
import random
import re
import sys

    
# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    SOCKS = set()   
    n_pairs = 0
    for sock in ar:
        if sock in SOCKS:
            SOCKS.remove(sock)
            n_pairs = n_pairs + 1
        else:
            SOCKS.add(sock)
    return n_pairs
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()