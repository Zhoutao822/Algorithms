#
# @lc app=leetcode.cn id=378 lang=python
#
# [378] 有序矩阵中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (53.05%)
# Total Accepted:    3K
# Total Submissions: 5.6K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。
# 
# 示例:
# 
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# 返回 13。
# 
# 
# 说明: 
# 你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n^2 。
# 
#
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        low, high = matrix[0][0], matrix[m-1][n-1]
        while low < high:
            mid = (low + high) // 2
            j = n - 1
            count = 0
            for i in range(m):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += (j+1)
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low

