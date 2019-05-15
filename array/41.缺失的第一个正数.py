#
# @lc app=leetcode.cn id=41 lang=python
#
# [41] 缺失的第一个正数
#
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i]-1]
        k = 0
        while k < n and nums[k] == k + 1:
            k += 1
        return k + 1