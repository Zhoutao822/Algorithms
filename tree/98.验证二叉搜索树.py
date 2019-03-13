#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (24.31%)
# Total Accepted:    16.2K
# Total Submissions: 65.9K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1:
#
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
#
#
# 示例 2:
#
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
#
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        ret = []

        def func(node, arr):
            if not node:
                return
            func(node.left, arr)
            arr.append(node.val)
            func(node.right, arr)

        func(root, ret)
        for i in range(len(ret) - 1):
            if ret[i] >= ret[i + 1]:
                return False
        return True

        # better
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     return self.helper(root, -1 << 63, (1 << 63) - 1)

    # def helper(self, root, minVal, maxVal):
    #     if root:
    #         if not minVal < root.val < maxVal:
    #             return False

    #         return self.helper(root.left, minVal, root.val) and self.helper(
    #             root.right, root.val, maxVal)
    #     return True
