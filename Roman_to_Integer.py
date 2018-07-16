class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #MCMXCIV
        #1000 + (-100+1000)+(-10+100)+(-1+5)  
        # 由i+1来确定i的正负号，如果s[i]<s[i+1] then -s[i]
        
        #s 是字符串 所以为了方便比较需要转化  这样转化可以？
        # I   =  1
        # V   =  5
        # X   =  10
        # L   =  50
        # C   =  100
        # D   =  500
        # M   =  1000
        
        #应该转化成一个字典
        # romDic = {'I':1,'V':5,'X':10,'L':50,'C':'100','D':500,'M':1000} #原来的字典c对应的值不小心加了引号变成了字符串导致的错误
        romDic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        result =  0
        flag =  0
        for i in range(len(s)-1):#一开始没有-1，索引溢出，但是-1之后，最后一位就没有比较到了 
            # TypeError: unorderable types: int() < str()  ??

            
            if romDic[s[i]] < romDic[s[i+1]]:
                flag = -1
            else:
                flag = 1
 
            # Line 36: TypeError: unsupported operand type(s) for +=: 'int' and 'str'
            result += flag*romDic[s[i]]
            
        return result+romDic[s[len(s)-1]] #最后一个直接加起来就行
