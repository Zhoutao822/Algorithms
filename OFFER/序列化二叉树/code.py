# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 请实现两个函数，分别用来序列化和反序列化二叉树
    def Serialize(self, root):
        # write code here
        ret = ''
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                ret += node.val
                queue.append(node.left)
                queue.append(node.right)
            else:
                ret += 'n'
            ret += ' '
        return ret

    def Deserialize(self, s):
        # write code here
        data = s.split()
        if data[0] == 'n': return None
        root = TreeNode(int(data[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if not node: continue
            node.left = TreeNode(int(data[i])) if data[i] != 'n' else None
            node.right = TreeNode(int(data[i+1])) if data[i+1] != 'n' else None
            i += 2
            queue.append(node.left)
            queue.append(node.right)
        return root