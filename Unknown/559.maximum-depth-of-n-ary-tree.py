#
# @lc app=leetcode.cn id=559 lang=python
#
# [559] Maximum Depth of N-ary Tree
#
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (64.35%)
# Total Accepted:    4.8K
# Total Submissions: 7.4K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# 给定一个 N 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 我们应返回其最大深度，3。
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。
#
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # top->down
        # if not root: return 0

        # def maxDep(node, depth):
        #     if not node.children: return depth
        #     return max([maxDep(child, depth + 1) for child in node.children])

        # return maxDep(root, 1)

        # down->top
        if not root: return 0
        if not root.children: return 1
        return max([self.maxDepth(child) for child in root.children]) + 1
