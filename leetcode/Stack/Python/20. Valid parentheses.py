#https://leetcode.com/submissions/detail/116515590/

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
#determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid 
#but "(]" and "([)]" are not.

class Solution(object):
    
    def isMatch(self, c1, c2):
        if (c1 == '[' and c2 ==']') or (c1 == '(' and c2 == ')') or (c1 == '{' and c2 == '}'):
            return True
        else:
            return False
        
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if stack and self.isMatch(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True