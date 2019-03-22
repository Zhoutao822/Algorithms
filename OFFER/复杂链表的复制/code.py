# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
import copy
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，
        # 另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
        # （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
        # return copy.deepcopy(pHead)
        if not pHead: return None
        cur_node = pHead
        while cur_node:
            clone_node = RandomListNode(cur_node.label)
            clone_node.next = cur_node.next
            cur_node.next = clone_node
            cur_node = cur_node.next.next
        
        cur_node = pHead
        while cur_node:
            cur_node.next.random = None if cur_node.random is None else cur_node.random.next
            cur_node = cur_node.next.next
        
        nHead = pHead.next
        cur_node = pHead
        while cur_node.next:
            tmp = cur_node.next
            cur_node.next = tmp.next
            cur_node = tmp
        return nHead
