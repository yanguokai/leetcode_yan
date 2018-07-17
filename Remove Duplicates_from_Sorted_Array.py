class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #明确规定需要注意时间和空间复杂度
        #Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        #可以定义常量空间
        
        #可以将重复的定义为0，统计非0的个数就行，0是不是里面的元素啊  可以设置为  最小值-1 也就是nums[0]-1
        
 #     #默认nums 不为空？
 #      if len(nums)==0:
 #           return 0
        
#         temp = nums[0]-1
#         print("定义一个标识重复的标签"+str(temp))
        
#         #那就是剩下不断的循环遍历咯
#         for i in range(len(nums)):
#             #避免非必要的循环，添加判断
#             if nums[i]!=temp:
#                 for j in range(i+1,len(nums)):
#                     if nums[i]==nums[j]:
#                         nums[j]=temp
                    
        # count = 0   
        # for str_temp in nums:
        #     if str_temp!=temp:
        #         # count ++
        #         count +=1
        # print (count)
        #不是直接返回长度吗
        #nums 也需要改变
        #定义两个下标变量，存储
        # start = 0
        # for i in range(len(nums)):
        #     #start 存储连续的不重复的最后一个下标位置
        #     #end 存放当前不重复的下标
        #     if nums[i]!=temp:
        #         nums[start] = nums[i]
        #         #如果start = i的时候下面就重复了
        #         # nums[i] = temp #不用管后面的情况
        #         start +=1
        # print(start)        
        # return start
        
        #太过于复杂导致运行时长超过限制
        #Time Limit Exceeded
        
        #默认nums 不为空？
        if len(nums)==0:
            return 0
        #可能是忘记有序了？ 所以多出了很多的比较  有序的话只要前后比较一次就行了
        start = 0
        index = 0
        for i in range(len(nums)):
            if nums[i]==nums[start]:
                #start 记录当前最后一个不重复的字符
                continue
            else:
                nums[start+1] = nums[i]
                start = start + 1
        return start+1
                
            
                
        
