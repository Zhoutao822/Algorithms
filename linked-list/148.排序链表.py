#
# @lc app=leetcode.cn id=148 lang=python
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (57.92%)
# Total Accepted:    10K
# Total Submissions: 16.9K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 
# 示例 1:
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2:
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 超时，冒泡不可行，使用归并排序
        # if not head:
        #     return head
        # p = head
        # count = 0
        # while p:
        #     p = p.next
        #     count += 1
        # for i in range(count-1, 0, -1):
        #     p = head
        #     while i > 0:
        #         if p.val > p.next.val:
        #             p.val, p.next.val = p.next.val, p.val
        #         p = p.next
        #         i -= 1
        # return head
        return None if not head else self.mergeSort(head)

    def mergeSort(self, head):
        if not head.next: return head
        p, q, pre = head, head, None
        while q and q.next:
            pre = p
            p = p.next
            q = q.next.next
        pre.next = None
        l = self.mergeSort(head)
        r = self.mergeSort(p)
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = ListNode(0)
        cur = dummy
        while l and r:
            if l.val <= r.val:
                cur.next = l
                cur = cur.next
                l = l.next
            else:
                cur.next = r
                cur = cur.next
                r = r.next
        if l: cur.next = l
        if r: cur.next = r
        return dummy.next