#
# @lc app=leetcode.cn id=179 lang=python
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (29.40%)
# Total Accepted:    4.7K
# Total Submissions: 15.3K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
# 
# 示例 1:
# 
# 输入: [10,2]
# 输出: 210
# 
# 示例 2:
# 
# 输入: [3,30,34,5,9]
# 输出: 9534330
# 
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
# 
#
from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums: return ''
        lmb = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
        arr = sorted(nums, key=cmp_to_key(lmb), reverse=True)
        return str((int(''.join([str(num) for num in arr]))))
n = [3,30,34,5,9]
print(Solution().largestNumber(n))
