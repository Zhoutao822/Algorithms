#
# @lc app=leetcode.cn id=204 lang=python
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (26.22%)
# Total Accepted:    16K
# Total Submissions: 58.8K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
# 
# 示例:
# 
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 
# 
#
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [1] * n
        res[0] = 0
        res[1] = 0
        i = 2
        while i * i < n:
            for j in range(2, (n-1)//i+1):
                res[i*j] = 0
            i += 1
        return sum(res)
