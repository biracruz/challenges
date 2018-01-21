class Solution(object):
    def multiply(self, numbers):
        total = 1
        for n in numbers:
            total *= n
        return total
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        response = []
        n = len(nums)                
        
        for i in range(n):
            response.append( self.multiply(nums[:i]+nums[i+1:]))
        return response