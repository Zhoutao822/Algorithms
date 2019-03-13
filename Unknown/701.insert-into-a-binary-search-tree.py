#
# @lc app=leetcode.cn id=701 lang=python
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (60.14%)
# Total Accepted:    2K
# Total Submissions: 3.3K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。
# 
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。
# 
# 例如, 
# 
# 
# 给定二叉搜索树:
# 
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# 
# 和 插入的值: 5
# 
# 
# 你可以返回这个二叉搜索树:
# 
# 
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
# 
# 
# 或者这个树也是有效的:
# 
# 
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   
# ⁠   1   3
# ⁠        \
# ⁠         4
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
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_node = TreeNode(val)
        if not root:
            return new_node
        cur = root
        while cur:
            if cur.val > val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = new_node
                    break
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = new_node
                    break
        return root

