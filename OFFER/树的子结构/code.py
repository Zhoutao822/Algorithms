# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
        if not pRoot2 or not pRoot1: return False
        if self.isSame(pRoot1, pRoot2):
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(
                pRoot1.right, pRoot2)

    def isSame(self, node1, node2):
        if not node2: return True
        if not node1 or node1.val != node2.val: return False
        return self.isSame(node1.left, node2.left) and self.isSame(
            node1.right, node2.right)
