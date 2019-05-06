#https://leetcode.com/submissions/detail/222968847/
"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        i = 0
        for c in s:
            if c in d:
                d[c] = -1
            else:
                d[c] = i
            i+=1
        print(d)
        for v in d.values():
            if v != -1:
                return v
        return -1


if __name__ == "__main__":
    S = Solution()
    print(S.firstUniqChar('loveleetcode'))
    print(S.firstUniqChar("aadadaad"))