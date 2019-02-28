# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur = headA
        la = 0
        while cur:
            la += 1
            cur = cur.next
        cur = headB
        lb = 0
        while cur:
            lb += 1
            cur = cur.next
        ha = headA
        hb = headB
        if la > lb:
            for _ in range(la - lb):
                ha = ha.next
        else:
            for _ in range(lb - la):
                hb = hb.next
        while ha:
            if ha == hb:
                return ha
            ha = ha.next
            hb = hb.next
        return None

        ha = headA
        hb = headB
        while(ha != hb):
            ha = headB if ha is None else ha.next
            hb = headA if hb is None else hb.next
        return ha