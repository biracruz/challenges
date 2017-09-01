#!/bin/python3


#https://www.hackerrank.com/challenges/plus-minus/submissions/code/53366980



import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

positives = len([i for i in arr if i > 0])/len(arr)
negatives = len([i for i in arr if i < 0])/len(arr)
zeros = len([i for i in arr if i == 0])/len(arr)

print(round(positives,6))
print(round(negatives,6))
print(round(zeros,6))