#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (64.02%)
# Total Accepted:    21.2K
# Total Submissions: 32.9K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # if not root:
        #     return []
        # ret = list()
        # def inorder(node):
        #     if node.left:
        #         inorder(node.left)
        #     ret.append(node.val)
        #     if node.right:
        #         inorder(node.right)
        # inorder(root)
        
        # return ret

        ret = list()
        stack = list()
        if not root:
            return ret
        p = root
        while p:
            stack.append(p)
            p = p.left
        while stack:
            p = stack.pop()
            ret.append(p.val)
            p = p.right
            while p:
                stack.append(p)
                p = p.left
        return ret
        
        

