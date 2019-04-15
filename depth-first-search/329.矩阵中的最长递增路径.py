#
# @lc app=leetcode.cn id=329 lang=python
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (36.73%)
# Total Accepted:    1.8K
# Total Submissions: 4.7K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个整数矩阵，找出最长递增路径的长度。
# 
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
# 
# 示例 1:
# 
# 输入: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径为 [1, 2, 6, 9]。
# 
# 示例 2:
# 
# 输入: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 
# 
#
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        # if not matrix or not matrix[0]:
        #     return 0
        # m, n = len(matrix)-1, len(matrix[0])-1
        # map = {}
        # def dfs(i, j, map):
        #     if (i, j) in map:
        #         return map[(i, j)]
        #     l = 1
        #     if i != 0 and matrix[i-1][j] > matrix[i][j]:
        #         l = max(l, 1+dfs(i-1, j, map))
        #     if i != m and matrix[i+1][j] > matrix[i][j]:
        #         l = max(l, 1+dfs(i+1, j, map))
        #     if j != 0 and matrix[i][j-1] > matrix[i][j]:
        #         l = max(l, 1+dfs(i, j-1, map))
        #     if j != n and matrix[i][j+1] > matrix[i][j]:
        #         l = max(l, 1+dfs(i, j+1, map))
        #     map[(i, j)] = l
        #     return l
        # max_length = 1
        # for i in range(m+1):
        #     for j in range(n+1):
        #         max_length = max(max_length, dfs(i, j, map))
        # return max_length

# better

        if not matrix or not matrix[0]:
            return 0
        
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        
        def dfs(i,j):
            if not dp[i][j]:
                dp[i][j]=1+max(
                dfs(i-1,j) if i>0 and matrix[i-1][j]>matrix[i][j] else 0,
                dfs(i+1,j) if i+1<m and matrix[i+1][j]>matrix[i][j] else 0,
                dfs(i,j-1) if j>0 and matrix[i][j-1]>matrix[i][j] else 0,
                dfs(i,j+1) if j+1<n and matrix[i][j+1]>matrix[i][j] else 0,
                )
            return dp[i][j]
        return max([dfs(i,j) for i in range(m) for j in range(n)])

