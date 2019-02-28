# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head.next:
            return None
        pre = ListNode(-1)
        pre.next = head
        fast = head
        slow = head
        for _ in range(n - 1):
            fast = fast.next
        while fast.next:
            pre = slow
            fast = fast.next
            slow = slow.next
        if slow == head:
            return head.next
        else:
            pre.next = pre.next.next
        return head