#https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

def is_pair(a, b):
    pairs = {'{':'}', '[':']','(':')','}':'{', ']':'[', ')':'('}
    if pairs[a] == b:
        return True
    else:
        return False

def is_matched(expression):
    stack = []
    for c in expression:
        if stack and is_pair(stack[-1], c):
            stack.pop()
        else:
            stack.append(c)
    if not stack:
        return True
    else:
        return False
    
t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"