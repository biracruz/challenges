#!/bin/python3
# https://www.hackerrank.com/challenges/diagonal-difference/submissions/code/53312378

# import sys


# n = int(input().strip())
# a = []
# for a_i in range(n):
#     a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
#     a.append(a_t)

# s1 = 0
# s2 = 0
# for i in range(n):
#     s1 = s1 + a[i][i]
#     s2 = s2 + a[n-i-1][i]
    
# print(abs(s1-s2))

#!/bin/python

import sys

def diagonalDifference(a):
    # Complete this function
    N = len(a)   
    d1 = [ a[i][i] for i in range(N)]
    d2 = [ a[i][j] for i,j in zip(range(N), reversed(range(N)))]
    return abs(sum(d1) - sum(d2))
    
if __name__ == "__main__":
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int,raw_input().strip().split(' '))
        a.append(a_temp)
    result = diagonalDifference(a)
    print result