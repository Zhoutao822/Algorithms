# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        # 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
        # 重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
        if not pHead or not pHead.next:
            return pHead
        if pHead.next and pHead.val == pHead.next.val:
            node = pHead.next
            while node != None and node.val == pHead.val:
                node = node.next
            return self.deleteDuplication(node)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead