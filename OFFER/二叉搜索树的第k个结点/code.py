# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    # 给定一棵二叉搜索树，请找出其中的第k小的结点。
    # 例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
    def KthNode(self, pRoot, k):
        # write code here
        ret = []
        stack = []
        p = pRoot
        if not pRoot:
            return None
        while p:
            stack.append(p)
            p = p.left
        while stack:
            p = stack.pop()
            ret.append(p)
            if len(ret) == k:
                return p
            p = p.right
            while p:
                stack.append(p)
                p = p.left
        return None