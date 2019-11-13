#!/bin/python3

#https://www.hackerrank.com/challenges/grading/submissions/code/53377298

import sys

def solve(grades):
    # Complete this function
    for i in range(len(grades)):
        if grades[i] >= 38 and grades[i] <= 40:
            grades[i] = 40
        
        if grades[i] > 40:                        
            next_m = (int((grades[i] / 5)) + 1)*5            
            if (next_m - grades[i]) < 3:
                grades[i] = next_m
                
    return grades

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))