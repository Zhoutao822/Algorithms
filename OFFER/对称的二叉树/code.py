# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        def isMirror(left, right):
            if left and not right:
                return False
            if right and not left:
                return False
            if not right and not left:
                return True
            if left.val != right.val:
                return False
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        return isMirror(pRoot, pRoot)