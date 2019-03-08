#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (66.98%)
# Total Accepted:    32K
# Total Submissions: 47.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # def bot(node):
        #     if not node:
        #         return 0
        #     l = bot(node.left)
        #     r = bot(node.right)
        #     return max([l, r]) + 1
        # return bot(root)
        depth = 0
        ret = 0
        def top(node, depth):
            nonlocal ret
            if not node:
                ret = max([depth, ret])
                return
            top(node.left, depth + 1)
            top(node.right, depth + 1)
        top(root, 0)
        return ret
            

