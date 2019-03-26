#
# @lc app=leetcode.cn id=212 lang=python
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (34.26%)
# Total Accepted:    1.6K
# Total Submissions: 4.9K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]'
#
# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
# 
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
# 
# 示例:
# 
# 输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# 
# 输出: ["eat","oath"]
# 
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
# 
# 提示:
# 
# 
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
# 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
# 
# 
#
class TrieNode:
    def __init__(self):
        self.root = {}
    
    def add(self, word):
        node = self.root
        for s in word:
            if s in node:
                node = node[s]
            else:
                node[s] = {}
                node = node[s]
        if 'is_end' not in node:
            node['is_end'] = True



class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        self.m, self.n = len(board), len(board[0])
        if self.m == 0 and self.n == 0:
            return res
        root = TrieNode()
        for word in words:
            root.add(word)
        visited = []

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root.root:
                    visited.append((i, j))
                    self.dfs(i, j, res, board[i][j], root.root[board[i][j]], visited, board)
                    visited.remove((i, j))
        return list(set(res))
    

    def dfs(self, i, j, res, cur_res, node, visited, board):
        
        if not node:
            return
        if 'is_end' in node:
            res.append(cur_res)
            node.pop('is_end')
        
        if i - 1 >= 0 and (i-1, j) not in visited and board[i-1][j] in node:
            visited.append((i-1, j))
            self.dfs(i-1, j, res, cur_res+board[i-1][j], node[board[i-1][j]], visited, board)
            visited.remove((i-1, j))
        if i + 1 < self.m and (i + 1, j) not in visited and board[i + 1][j] in node:
            visited.append((i + 1, j))
            self.dfs(i+1, j, res, cur_res+board[i+1][j], node[board[i+1][j]], visited, board)
            visited.remove((i+1, j))            
        if j - 1 >= 0 and (i, j-1) not in visited and board[i][j-1] in node:
            visited.append((i, j-1))
            self.dfs(i, j-1, res, cur_res+board[i][j-1], node[board[i][j-1]], visited, board)
            visited.remove((i, j-1))
        if j + 1 < self.n and (i, j+1) not in visited and board[i][j+1] in node:
            visited.append((i, j+1))
            self.dfs(i, j+1, res, cur_res+board[i][j+1], node[board[i][j+1]], visited, board)
            visited.remove((i, j+1))

# better
# class Trie(object):
#     def __init__(self):
#         self.root = {}       
    
#     def insert(self, word):
#         """
#         Inserts a word into the trie.
#         :type word: str
#         :rtype: void
#         """
#         curNode = self.root
#         for i in word:
#             if i not in curNode:
#                 curNode[i] = {}
#             curNode = curNode[i]
#         curNode["#"] = True

    

# class Solution(object):
#     def findWords(self, board, words):
#         """
#         :type board: List[List[str]]
#         :type words: List[str]
#         :rtype: List[str]
#         """
#         row = len(board) - 1
#         colum = len(board[0]) - 1
        
#         res = []

#         def find(x, y, p, curNode):

#             p += board[x][y]
#             if curNode.get("#") is not None and curNode["#"] is True:
#                 res.append(p[:len(p)])
#             t = board[x][y]
#             board[x][y] = "-1"
#             if x + 1 <= row and board[x + 1][y] in curNode:
#                 find(x + 1, y, p, curNode[board[x + 1][y]])
#             if x - 1 >= 0 and board[x - 1][y] in curNode:
#                 find(x - 1, y, p, curNode[board[x - 1][y]])
#             if y + 1 <= colum and board[x][y + 1] in curNode:
#                 find(x, y + 1, p, curNode[board[x][y + 1]])
#             if y - 1 >= 0 and board[x][y - 1] in curNode:
#                 find(x, y - 1, p, curNode[board[x][y - 1]])
#             board[x][y] = t
#         node = Trie()
#         for i in words:
#             node.insert(i)
#         for x in range(row + 1):
#             for y in range(colum + 1):
#                 if board[x][y] in node.root:
#                     find(x, y, "", node.root[board[x][y]])

#         return list(set(res))
words = ["oath","pea","eat","rain"] 
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
print(Solution().findWords(board, words))