# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        # 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
        if not pRoot:
            return []
        ret = []
        queue = [pRoot]
        while queue:
            tmp = []
            count = len(queue)
            for _ in range(count):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(tmp)
        return ret