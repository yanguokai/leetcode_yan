class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #实现基本的函数

        #一开始以为这里还需要判断haystack的状态
        #也不清楚python中字符串判空，和长度为0是一样的?
        # if not needle:
        if len(needle)==0:
            return 0
            
        #可以直接判断字符串相等的，没有必要去单个字符比较！！！
        for i in range(len(haystack)):
            if i + len(needle)<=len(haystack):
                if haystack[i:i+len(needle)]==needle:
                    return i
        return -1
                    
                    
        
