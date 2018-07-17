class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x<0:
            flag = -1
        else:
            flag = 1
        x = flag*x
        
        result = 0 
        while x>0:
            result = result*10 + x%10
            print("result:"+str(result))
            x = x//10 #问题出在python的整除上面
            print("x:"+str(x))
      
        if result>2147483647:
            return 0
        else:
            return result*flag
        
        
