# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        url: https://leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/745/
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        hasCycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                hasCycle = True
                break
        if hasCycle:
            new = head
            while new != fast:
                new = new.next
                fast = fast.next
            return new
        else:
            return None