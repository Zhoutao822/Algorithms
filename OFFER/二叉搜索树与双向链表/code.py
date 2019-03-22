# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        # 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
        # 要求不能创建任何新的结点，只能调整树中结点指针的指向。
        
        # 任意一个非叶结点的前驱必定是树中左子树的最右叶结点，后继必定是右子树的最左结点
        # 递归

        if not pRootOfTree: return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right: return pRootOfTree

        left = pRootOfTree.left
        self.Convert(left)
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left = left
            left.right = pRootOfTree

        right = pRootOfTree.right
        self.Convert(right)
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right = right
            right.left =pRootOfTree

        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left
        return pRootOfTree

