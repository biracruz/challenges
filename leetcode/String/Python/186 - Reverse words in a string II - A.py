"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array
"""

#my submission
#https://leetcode.com/submissions/detail/115688650/
class Solution:
    
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        #extra space
        st = ''.join(s) #transforms to str to split        O(n) ?
        #extra space
        sp = st.split() # splited s O(k)
        #extra space
        inv_w = sp[::-1] # inverted words withou blank space O(k)
        #extra space
        inv_s_bs = ' '.join(inv_w) # inverted str with blank spaces
        s[0:] = list(inv_s_bs)
 