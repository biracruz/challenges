#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

def number_needed(a, b):
    A = {i : a.count(i) for i in a}
    B = {i : b.count(i) for i in b}
    intersections = 0
    
    for l in A:
        if l in B:
            intersections = intersections + min(A[l], B[l])
    
    return sum(A.values()) + sum(B.values()) - 2* intersections

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)