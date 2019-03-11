#
# @lc app=leetcode.cn id=652 lang=python
#
# [652] 寻找重复的子树
#
# https://leetcode-cn.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (48.34%)
# Total Accepted:    887
# Total Submissions: 1.8K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
# 
# 两棵树重复是指它们具有相同的结构以及相同的结点值。
# 
# 示例 1：
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# 
# 下面是两个重复的子树：
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# 
# 和
# 
# ⁠   4
# 
# 
# 因此，你需要以列表的形式返回上述重复子树的根结点。
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        visited = dict()
        def helper(root):
            if not root:
                return "#"
            s = helper(root.left)+"," + helper(root.right) + "," + str(root.val)
            if s in visited.keys():
                if visited[s] == 1:
                    res.append(root)
                visited[s] += 1
            else:
                visited[s] = 1
            return s
        helper(root)
        return res

