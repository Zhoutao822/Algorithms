#
# @lc app=leetcode.cn id=171 lang=python
#
# [171] Excel表列序号
#
# https://leetcode-cn.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (63.21%)
# Total Accepted:    11.4K
# Total Submissions: 18.1K
# Testcase Example:  '"A"'
#
# 给定一个Excel表格中的列名称，返回其相应的列序号。
# 
# 例如，
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: "A"
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入: "AB"
# 输出: 28
# 
# 
# 示例 3:
# 
# 输入: "ZY"
# 输出: 701
# 
# 致谢：
# 特别感谢 @ts 添加此问题并创建所有测试用例。
# 
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        def num(s):
            return ord(s) - 64
        ret = 0
        for c in s:
            ret = 26 * ret + num(c)
        return ret
        
a = 'AB'

print(Solution().titleToNumber(a))

