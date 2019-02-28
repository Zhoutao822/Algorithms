
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        head1, head2 = head, head.next
        cur1, cur2 = head1, head2
        while True:
            if not cur1.next or not cur2.next:
                break
            cur1.next = cur1.next.next
            cur1 = cur1.next
            cur2.next = cur2.next.next
            cur2 = cur2.next
        cur1.next = head2
        return head1


        # better
        # if not head or not head.next:
        #     return head
        # p1 = head.next
        # p2 = head
        # while p1 and p1.next:
        #     q = p1.next
        #     p1.next = q.next
        #     q.next = p2.next
        #     p2.next = q
        #     p2 = q
        #     p1 = p1.next
        # return head
