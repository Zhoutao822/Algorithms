#
# @lc app=leetcode.cn id=23 lang=python
#
# [23] 合并K个排序链表
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return
        l, r = 0, len(lists)-1
        return self.merge(lists, l, r)
    
    def merge(self, lists, l, r):
        if l == r:
            return lists[l]
        mid = l + (r - l) // 2
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid + 1, r)
        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

