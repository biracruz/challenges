#https://leetcode.com/submissions/detail/222980608/
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
import collections
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for n in count:
            if count[n] == 1:
                return n

if __name__ == "__main__":
    S = Solution()
    assert S.singleNumber([2,2,1]) == 1
    assert S.singleNumber([4,1,2,1,2]) == 4