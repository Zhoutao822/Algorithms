#
# @lc app=leetcode.cn id=130 lang=python
#
# [130] 被围绕的区域
#
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        def mark(i, j):
            board[i][j] = 0
            if i > 0 and board[i-1][j] == 'O':
                mark(i-1, j)
            if i < m-1 and board[i+1][j] == 'O':
                mark(i+1, j)
            if j > 0 and board[i][j-1] == 'O':
                mark(i, j-1)
            if j < n-1 and board[i][j+1] == 'O':
                mark(i, j+1)
        for j in range(n):
            if board[0][j] == 'O':
                mark(0, j)
            if board[m-1][j] == 'O':    
                mark(m-1, j)
        for i in range(m):
            if board[i][0] == 'O':
                mark(i, 0)
            if board[i][n-1] == 'O':
                mark(i, n-1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        
b = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Solution().solve(b)
print(b)
