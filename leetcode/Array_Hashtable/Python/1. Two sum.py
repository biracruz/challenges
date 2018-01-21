#https://leetcode.com/submissions/detail/116039472/
#Given an array of integers, return indices of the two numbers such that they add up to a specific targe#
#You may assume that each input would have exactly one solution, and you may not use the same element twic#
#Example:
#Given nums = [2, 7, 11, 15], target = #
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dic = {}
        
        #preparing map
        for n, i in zip(nums, range(0, len(nums))):
            if n in nums_dic:
                nums_dic[n].append(i)
            else:
                nums_dic[n] = [i]
        
        #for each number find the complement and check if 
        #it exists on original array
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in nums_dic:
                last = nums_dic[complement][-1]
                if i != last:
                    return [i, last ]