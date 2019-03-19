# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        # 输入一个链表，反转链表后，输出新链表的表头。
        pre = None
        while pHead:
            pNext = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = pNext
        return pre