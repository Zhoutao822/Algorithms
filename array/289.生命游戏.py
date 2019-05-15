#
# @lc app=leetcode.cn id=289 lang=python
#
# [289] 生命游戏
#
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = self.helper(i, j, board)
                if count < 2 and board[i][j] == 1:
                    board[i][j] = 2
                elif count > 3 and board[i][j] == 1:
                    board[i][j] = 2
                elif count == 3 and board[i][j] == 0:
                    board[i][j] = -1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1



    def helper(self, i, j, a):
        count = 0
        if (i-1) >= 0 and a[i-1][j] > 0: count += 1
        if (i-1) >= 0 and (j-1) >= 0 and a[i-1][j-1] > 0: count += 1
        if (j-1) >= 0 and a[i][j-1] > 0: count += 1
        if (i-1) >= 0 and (j+1) < len(a[0]) and a[i-1][j+1] > 0: count += 1
        if (i+1) < len(a) and a[i+1][j] > 0: count += 1
        if (i+1) < len(a) and (j-1) >= 0 and a[i+1][j-1] > 0: count += 1
        if (i+1) < len(a) and (j+1) < len(a[0]) and a[i+1][j+1] > 0: count += 1
        if (j+1) < len(a[0]) and a[i][j+1] > 0: count += 1
        return count

