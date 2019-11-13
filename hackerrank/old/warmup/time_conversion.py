#!/bin/python3
#https://www.hackerrank.com/challenges/time-conversion/submissions/code/53373248

import sys

def timeConversion(s):
    # Complete this function
    mer = s[-2:]        
    time = ""
    #PM
    if mer == 'PM':
        if s[:2] == "12":
            h = 12
        else:
            h = 12 + int(s[:2])
            if h < 10:
                h = "0"+str(h)                
        time = str(h) + s[2:-2]
    #AM keep...
    else:
        #if is midnight
        if s[:2] == "12":
            h = "00"
            time = str(h) + s[2:-2]
        else:
            time = s[:-2]
    return time
        
s = input().strip()
result = timeConversion(s)
print(result)