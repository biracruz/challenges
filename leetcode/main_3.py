"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
"""
Say that two words consists in an Anagram:
1: same numbers of different letters
2: the same letters

groups
[
    ["eat","tea"],
    ["tan"],
]
"""


"""
Say that two words consists in an Anagram:
1: same numbers of different letters
2: the same letters

groups
[
    ["eat","tea"],
    ["tan"],
]
"""


class Solution:
    
    def check_group(self, groups, word):
        for i, group in enumerate(groups):
            if self.anagram(group, word):
                return i
        return -1
            
        
    def anagram(self, words_list, word):
        try:
            last_word = words_list[-1]
        except IndexError:
            return False
        
        if len(last_word) != len(word):
            return False
        
        for c in word:
            if c not in last_word:
                return False
        return True
            
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []                
        groups.append([strs[0]])
            
        for word in strs[1:]:           
            for i, group in enumerate(groups):                
                if self.anagram(group, word):
                    group.append(word)                    
            groups.append([word])
        return groups
        

sol = Solution()
#assert sol.anagram(['any','ate'],'eat') is True
#assert sol.anagram([], '') is False
G = [
  ["ate","eat","tea"],
  ["nat"]
]
assert sol.check_group(G, "tan") is 1
assert sol.anagram(["ate"], "tan") is False
assert sol.anagram(["nat"], "tan") is True