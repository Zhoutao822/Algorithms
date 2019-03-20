# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        # 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
        if not pHead1: return pHead2
        if not pHead2: return pHead1
        head = ListNode(None)
        cur1 = pHead1
        cur2 = pHead2
        cur = head
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next
        cur.next = cur1 if not cur2 else cur2
        return head.next