class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #首先为负的时候，需要返回false
        if x<0:
            return False
        #从左从右同时比较，相同则true
        #如何遍历 int,还不能将整形转化成string
        
        #取整取余吗
        #12321   'int' has no len() 不能够直接获取int的长度 先遍历一遍
        
        div = 1
        #注意python中while和for
        while x/div>=10:  
            div*=10
        while x>0:
            l = x//div
            r = x%10
            if l!=r:
                return False
            else:
                #需要去掉首尾两个数  比如123321  ---- 2332
                x %=div  #取余获取首位以外的值
                x //=10  #再取整获取末尾以外的值
                div/=100 #更新div 比较一次 会同时去掉首尾两端 ，所以需要除以100
        return True
        
        
        
