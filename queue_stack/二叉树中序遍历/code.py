# Definition for a binary tree node.
# url: https://leetcode-cn.com/explore/learn/card/queue-stack/219/stack-and-dfs/887/
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root: return []
        stack = [root]
        ret = []
        visited = set()
        while stack:
            cur = stack[-1]
            if cur.left is not None and cur.left not in visited:
                stack.append(cur.left)
                continue
            else:
                ret.append(cur.val)
                stack.pop()
                visited.add(cur)
            if cur.right is not None and cur.right not in visited:
                stack.append(cur.right)
        return ret

