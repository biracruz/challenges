#https://leetcode.com/submissions/detail/222968847/
"""
Approach 1: Linear time solution
The best possible solution here could be of a linear time because to ensure that the character is unique you have to check the whole string anyway.

The idea is to go through the string and save in a hash map the number of times each character appears in the string. That would take \mathcal{O}(N)O(N) time, where N is a number of characters in the string.

And then we go through the string the second time, this time we use the hash map as a reference to check if a character is unique or not.
If the character is unique, one could just return its index. The complexity of the second iteration is \mathcal{O}(N)O(N) as well.



Complexity Analysis

Time complexity : \mathcal{O}(N)O(N) since we go through the string of length N two times.
Space complexity : \mathcal{O}(N)O(N) since we have to keep a hash map with N elements.
Analysis written by @liaison and @andvary
"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        index = 0
        for ch in s:
            if count[ch] == 1:
                return index
            else:
                index += 1       
        return -1


if __name__ == "__main__":
    S = Solution()
    print(S.firstUniqChar('loveleetcode'))
    print(S.firstUniqChar("aadadaad"))