# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #两个有序的链表进行融合
        #固定一条，将另一条添加到固定的链表上
        
        #应该是有很多的属性和方法不清楚
        #直接使用l1和l2来遍历
        # p = l1
        # q = l2
        #是不是应该有l3啊
        #python 创建一个空结点
        l3 = ListNode(-1)
        head = l3
        
        #链表的长度应该没有属性获取
        #固定p 
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next
            l3 = l3.next
        
        #判断是什么原因导致退出循环
        if l1:
            l3.next = l1
        else:
            l3.next = l2
        
        return head.next

                
            
        
        
