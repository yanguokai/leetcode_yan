class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #转化成计算机可以识别的数据
        #()[]{}
        l_1 = '('
        l_2 = '['
        l_3 = '{'
        
        l_list = [l_1,l_2,l_3]
        
        
        r_1 = ')'
        r_2 = ']'
        r_3 = '}'
        
        r_list = [r_1,r_2,r_3]
        #         #构建键值对会不会更好比配一些
        p_dic = {'(':')','[':']','{':'}'}
                
        #需要构建一个栈吗？
        stack = []
        for str_temp in s:
            if str_temp in l_list:
                stack.append(str_temp)
            else:
                # Line 30: IndexError: pop from empty list  出栈之前没有判空
                if len(stack)>0:
                    temp_pop = stack.pop()
                    if(str_temp!=p_dic[temp_pop]):
                        return False
                else:
                    return False
        #需要进行判断最后是否栈空
        if len(stack)!=0:
            return False
        return True
                    
                    
        
        



#         python 中的数据结构还没有了解，
        

        

            
