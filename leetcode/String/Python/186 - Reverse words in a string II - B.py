"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

Related problem: Rotate Array
"""

class Solution:    
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        s.reverse() #reverse all list
        word_start = 0
        for i in range(len(s)):
            #now you just have to correct the words
            if s[i] == " ":
                s[word_start: i] = reversed(s[word_start: i]) #reverse again to put word correctly
                word_start = i + 1 # next word start is after blank space
        #last word without blank space in the end
        s[word_start:] = reversed(s[word_start:])

def main():
    obj = Solution()
    s = ['a', ' ', 'b']
    obj.reverseWords(s)
    #expected ['b', ' ', 'a']
    print(s)

if __name__ == '__main__':
    main()
 