#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (44.94%)
# Total Accepted:    22.9K
# Total Submissions: 50.7K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠    1
# ⁠   / \
# ⁠  2   2
# ⁠ / \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠   3   3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # queue = [root]
        # while queue:
        #     tmp = []
        #     count = len(queue)
        #     while count > 0:
        #         node = queue.pop(0)
        #         tmp.append(node.val if node else None)
        #         if node:
        #             queue.append(node.left)
        #             queue.append(node.right)
        #         count -= 1
        #     if tmp != list(reversed(tmp)):
        #         return False
        # return True

        def isMirror(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val == r.val:
                return isMirror(l.left, r.right) and isMirror(l.right, r.left)
            else:
                return False
        return isMirror(root, root)

