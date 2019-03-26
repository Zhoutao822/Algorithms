#
# @lc app=leetcode.cn id=152 lang=python
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (31.91%)
# Total Accepted:    6.8K
# Total Submissions: 20.5K
# Testcase Example:  '[2,3,-2,4]'
#
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums_re = nums[::-1]
        # for i in range(1, len(nums)):
        #     nums[i] *= nums[i-1] or 1
        #     nums_re[i] *= nums_re[i-1] or 1
        # return max(max(nums), max(nums_re))

        Max = -float('inf')
        imax = 1
        imin = 1
        for num in nums:
            if num < 0:
                imax, imin = imin, imax
            imax = max(imax * num, num)
            imin = min(imin * num, num)
            Max = max(Max, imax)
        return Max

n = [-2, 0, -1]
import random
random.shuffle(n)
print(n)
print(Solution().maxProduct(n))