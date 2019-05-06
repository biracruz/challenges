#https://leetcode.com/submissions/detail/227176190/

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

"""
in : {[]}

"" -> {
"" -> {   [
"" -> {   [   ] (match) -> pop
"" -> {   }     (match) -> pop
""  empty? is Valid

"""
class Solution:
    
    def match(self, c1 : str, c2: str) -> bool:
        map = {"(": ")", ")":"(", 
               "[": "]", "]":"[",
               "{":"}", "}":"{"}
        if map.get(c1, None) == c2:
            return True
        else:
            return False
    
    def isValid(self, s: str) -> bool:
        
        stack = [] # the end is the top
        
        for c in s:
            if stack and self.match(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True
        
 


sol = Solution()
assert sol.match("{","}") is True
assert sol.match("]", "[") is True
assert sol.isValid("") is True
assert sol.isValid("[") is False
assert sol.isValid("()") is True
assert sol.isValid("()[]{}") is True
assert sol.isValid("(]") is False
assert sol.isValid("([)]") is False
assert sol.isValid("{[]}") is True