class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
            #默认nums 不为空？
        if len(nums)==0:
            return 0
        #用start来记录第一个为val值的地方
        #应该使用左右两个指针来夹逼,我一开始想着用一个start 和一个index来做指针
        left = 0
        right = len(nums)-1
        #左边存储不为val的值，右边存储为val的值
        while left<=right:
            #下面的每次判断left 和 right的判断是为了什么？
            while left<=right and nums[left]!=val:
                left+=1
            while left<=right and nums[right]==val:
                right-=1
            if left<right:
                nums[left]=nums[right]
                right -=1
                left +=1
        return right+1
            
