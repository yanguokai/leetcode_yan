class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            temp = target - nums[i]
            
            for j in range(i+1,len(nums)):
                if temp==nums[j]:
                    return [i,j]
        return [None,None]
        
        
        
        
