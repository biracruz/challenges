#created by biracruz on 23 May 2012

'''
Given an array of N integers, can you find the sum of its elements?

Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers representing the array's elements.

Output Format

Print the sum of the array's elements as a single integer.

Sample Input

6
1 2 3 4 10 11
Sample Output

31
Explanation

We print the sum of the array's elements, which is: 
1 + 2 + 3 + 4 + 10 + 11 = 31.
'''



#!/bin/python

import sys
import operator

    

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
s = reduce(operator.add, arr)
print s