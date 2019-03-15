#
# @lc app=leetcode.cn id=589 lang=python
#
# [589] N-ary Tree Preorder Traversal
#
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (65.78%)
# Total Accepted:    4.7K
# Total Submissions: 7K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# 给定一个 N 叉树，返回其节点值的前序遍历。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其前序遍历: [1,3,5,6,2,4]。
# 
# 
# 
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 递归
        # ret = []
        # if not root: return ret
        # def pre(node, arr):
        #     if node:
        #         arr.append(node.val)
        #         for child in node.children:
        #             pre(child, arr)
        #     return arr
        # return pre(root, ret)

        # 迭代
        if not root: return []
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                for child in reversed(node.children):
                    stack.append(child)
        return ret

