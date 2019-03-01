#
# @lc app=leetcode.cn id=138 lang=python
#
# [138] 复制带随机指针的链表
#
# https://leetcode-cn.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (24.28%)
# Total Accepted:    3.8K
# Total Submissions: 15.7K
# Testcase Example:  '{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}'
#
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 
# 要求返回这个链表的深拷贝。 
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：
# 
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 
# 解释：
# 节点 1 的值是 1，它的下一个指针和随机指针都指向节点 2 。
# 节点 2 的值是 2，它的下一个指针指向 null，随机指针指向它自己。
# 
# 
# 
# 
# 提示：
# 
# 
# 你必须返回给定头的拷贝作为对克隆列表的引用。
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        
        cur_head = head
        while cur_head:
            val = cur_head.val
            new_node = Node(val, None, None)
            new_node.next = cur_head.next
            cur_head.next = new_node
            cur_head = new_node.next
        
        cur_head = head
        while cur_head:
            new_node = cur_head.next
            if cur_head.random:
                new_node.random = cur_head.random.next
            cur_head = new_node.next
        
        cur_head = head
        new_head = head.next
        while cur_head is not None and cur_head.next:
            next_node = cur_head.next
            cur_head.next = next_node.next
            cur_head = next_node
        
        return new_head


# better
        # if not head:
        #     return 
        
        # res = Node(head.val, None, None)
        # n1 = head.next
        # n2 = res
        # lists = {head:res}
        # while n1:
        #     n2.next = Node(n1.val, None, None)
        #     lists[n1] = n2.next
        #     n1 = n1.next
        #     n2 = n2.next
        # lists[None] = None
        # n1 = head
        # n2 = res
        # while n1:
        #     n2.random = lists[n1.random]
        #     n2 = n2.next
        #     n1 = n1.next
        # return res


# simple

"""
# # Definition for a Node.
# class Node(object):
#     def __init__(self, val, next, random):
#         self.val = val
#         self.next = next
#         self.random = random
# """
# class Solution(object):
#     def copyRandomList(self, head):
#         """
#         :type head: Node
#         :rtype: Node
#         """
#         return copy.deepcopy(head)