#
# @lc app=leetcode.cn id=238 lang=python
#
# [238] 除自身以外数组的乘积
#
# https://leetcode-cn.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (57.85%)
# Total Accepted:    7.2K
# Total Submissions: 12K
# Testcase Example:  '[1,2,3,4]'
#
# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i]
# 之外其余各元素的乘积。
# 
# 示例:
# 
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
# 
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        left, right = [1], [1]
        nums_re = nums[::-1]
        for i in range(1, len(nums)):
            left.append(nums[i-1] * left[-1])
            right.append(nums_re[i-1] * right[-1])
        return [x * y for x, y in zip(left,right[::-1])]
n = [1,2,3,4]
print(Solution().productExceptSelf(n))