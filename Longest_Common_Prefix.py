class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #可以遍历一个字符串，然后去其他的字符串里面去查找
        
        #需要先判断strs空吗？
        if len(strs)==0:
            return ""
        
        #要如何判断
        str_cp = ""
        #添加最小长度判断，遍历最小长度字符串
        min_len = len(strs[0])
        min_i = 0
        for str_i in strs:
            if min_len>len(str_i):
                min_len = len(str_i)
        
        for i in range(min_len): #没有考虑到长度问题
            temp = strs[0][i]
            print("遍历第一个字符串"+temp)
            for s in strs:
                if temp!=s[i]:
                    print(s[i])
                    # return ""
                    # break
                    return str_cp
            str_cp += s[i]
            
        return str_cp
                
            
            
            
        #失败的时候返回一个空字符创，否则返回最长公共前缀部分
        # return ""
