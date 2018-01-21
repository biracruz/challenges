
class Solution(object):
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # test = [1,2,3,4]
        # pv = [1 , 1,2,6]
        # nt = [24,12,4,1]
        # out= [24,12,8,6]
        
        response = []
        n = len(nums)                
        m = 1
        # pv = [1,1,2,6]
        response.append(1) #pv = [1]
        for i in range(1, n):            
            m = m * nums[i - 1]
            response.append(m)
        # nt = [24,12,4,1]
        m = 1
        for i in range(n-2, -2, -1):
            response[i+1] = response[i+1] * m
            m = m * nums[i+1]
            
        return response