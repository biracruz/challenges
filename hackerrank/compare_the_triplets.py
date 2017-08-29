#!/bin/python3

import sys

def check_pair(n1, n2):
    if ((n1 - n2) == 0):
        return (0, 0)
    if (n1 > n2 ):
        return (1, 0)
    else:
        return (0, 1)
    
def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    A_B = []
    A_B.append(check_pair(a0, b0))
    A_B.append(check_pair(a1, b1))
    A_B.append(check_pair(a2, b2))
    return [sum([t[0] for t in A_B]), sum([t[1] for t in A_B])]

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))