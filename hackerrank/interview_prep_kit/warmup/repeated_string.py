#!/bin/python3
# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D=warmup
# https://www.hackerrank.com/challenges/repeated-string/submissions/code/130341111?h_l=interview&isFullScreen=false&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D%5B%5D%5B%5D%5B%5D=warmup

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    ocurrences = s.count('a')
    int_div = n // l
    total_ocurrences = int_div * ocurrences
    remain_posicions = n - (int_div * l)
    remain_ocurrences = s[0:remain_posicions].count('a')
    total_ocurrences = total_ocurrences + remain_ocurrences
    return total_ocurrences

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
