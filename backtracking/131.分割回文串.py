#
# @lc app=leetcode.cn id=131 lang=python
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (61.59%)
# Total Accepted:    4.8K
# Total Submissions: 7.8K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回 s 所有可能的分割方案。
# 
# 示例:
# 
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
#
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.ret = []
        self.par(s, 0, [])
        return self.ret

    def par(self, s, i, arr):
        if i == len(s):
            self.ret.append(arr)
        for m in range(i+1, len(s)+1):
            if self.helper(s[i:m]):
                self.par(s, m, arr + [s[i:m]])      

    def helper(self, s):
        return s == s[::-1]

s = 'aab'
print(Solution().partition(s))
