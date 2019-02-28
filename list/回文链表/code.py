# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        pre = None
        slow = slow.next
        while slow:
            next = slow.next
            slow.next = pre
            pre = slow
            slow = next
        while pre and head:
            if pre.val != head.val:
                return False
            else:
                pre = pre.next
                head = head.next
        return True