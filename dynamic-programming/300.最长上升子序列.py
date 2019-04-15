#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (38.93%)
# Total Accepted:    10.7K
# Total Submissions: 26.4K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 
# 示例:
# 
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
# 说明:
# 
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
# 
# 
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
# 
#
class Solution(object):
    # def lengthOfLIS(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     if not nums: return 0
    #     dp = [0] * len(nums)
    #     dp[-1] = 1
    #     for i in range(len(nums)-2, -1, -1):
    #         arr = [dp[j] for j in range(i+1, len(nums)) if nums[j] > nums[i]]
    #         dp[i] = max(arr) + 1 if arr else 1
    #     return max(dp)


    # better

    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

n = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(n))
