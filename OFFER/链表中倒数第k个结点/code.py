# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # 输入一个链表，输出该链表中倒数第k个结点。
        fast = slow = head
        if not head or k == 0: return None
        for _ in range(k-1):
            if not fast.next: return None
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow
        # better
        # l=[]
        # while head!=None:
        #     l.append(head)
        #     head=head.next
        # if k>len(l) or k<1:
        #     return
        # return l[-k]