# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        # 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
        queue = [root]
        ret = []
        if not root: return []
        while queue:
            count = len(queue)
            for _ in range(count):
                node = queue.pop(0)
                ret.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ret
                