# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        # 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
        # 第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
        if not pRoot:
            return []
        queue = [pRoot]
        ret = []
        flag = True
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
            if flag:
                ret.append(tmp)
                flag = False
            else:
                ret.append(tmp[::-1])
                flag = True
        return ret