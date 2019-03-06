#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.83%)
# Total Accepted:    6.4K
# Total Submissions: 16.1K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
# 
# 说明：不要使用任何内置的库函数，如  sqrt。
# 
# 示例 1：
# 
# 输入：16
# 输出：True
# 
# 示例 2：
# 
# 输入：14
# 输出：False
# 
# 
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        if num == 1:
            return True
        while x ** 2 > num:
            x = (num + x ** 2) // (2 * x)
            if x ** 2 == num:
                return True
        return False

