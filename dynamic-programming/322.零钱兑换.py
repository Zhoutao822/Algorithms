#
# @lc app=leetcode.cn id=322 lang=python
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (28.25%)
# Total Accepted:    8.4K
# Total Submissions: 27.2K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 示例 1:
# 
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 
# 示例 2:
# 
# 输入: coins = [2], amount = 3
# 输出: -1
# 
# 说明:
# 你可以认为每种硬币的数量是无限的。
# 
#
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        if amount < min(coins): return -1
        dp = [amount] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            arr = [dp[i - coin] for coin in coins if (i - coin) >= 0 and dp[i-coin] != -1]
            dp[i] = min(arr) + 1 if arr else -1
        return dp[amount]
        
coins = [1, 2, 5]
amount = 11
print(Solution().coinChange(coins, amount))
