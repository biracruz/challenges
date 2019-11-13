#!/bin/python3
# https://www.hackerrank.com/challenges/counting-valleys/problem
# https://www.hackerrank.com/challenges/counting-valleys/submissions/code/130337989
import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    steps = {'U':1,'D':-1,'S':0}
    inside_valley = False
    step_sum = 0
    for step in s:
        value = steps.get(step)
        step_sum = value + step_sum
        if step_sum < 0 and not inside_valley:
            inside_valley = True
        
        if step_sum == 0 and inside_valley:
            #got out
            inside_valley = False
            valleys = valleys + 1
    return valleys
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
