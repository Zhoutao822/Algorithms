# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        # 输入两个链表，找出它们的第一个公共结点。
        list = []
        while pHead1:
            list.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2:
            if pHead2.val in list:
                return pHead2
            else:
                pHead2 = pHead2.next
        return None # 返回空等价于不返回，python

        # better
        # p1 = pHead1
        # p2 = pHead2
        # while p1 != p2:
        #     p1 = pHead2 if p1 is None else p1.next
        #     p2 = pHead1 if p2 is None else p2.next
        # return p1
