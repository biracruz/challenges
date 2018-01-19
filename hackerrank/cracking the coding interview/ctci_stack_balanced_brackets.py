#https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

def is_matched(expression):
    stack = []
    pairs = {'{':'}', '[':']','(':')','}':'{', ']':'[', ')':'('}
    for c in expression:
        if stack and pairs[stack[-1]] == c:
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