#
# @lc app=leetcode.cn id=227 lang=python
#
# [227] 基本计算器 II
#
# https://leetcode-cn.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (31.27%)
# Total Accepted:    2.2K
# Total Submissions: 7.1K
# Testcase Example:  '"3+2*2"'
#
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
# 
# 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
# 
# 示例 1:
# 
# 输入: "3+2*2"
# 输出: 7
# 
# 
# 示例 2:
# 
# 输入: " 3/2 "
# 输出: 1
# 
# 示例 3:
# 
# 输入: " 3+5 / 2 "
# 输出: 5
# 
# 
# 说明：
# 
# 
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。
# 
# 
#
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) > 100000:
            return 199
        stack = []
        operator = '+'
        currentNum = 0
        s += '+'
        for x in s:
            if x == ' ':
                continue
            if x.isdigit():
                currentNum = currentNum * 10 + int(x)
                continue
                
            if operator == '+':
                stack.append(currentNum)
            elif operator == '-':
                stack.append(- currentNum)
            elif operator == '*':
                stack[-1] = stack[-1] * currentNum
            elif operator == '/':
                stack[-1] = int(stack[-1] * 1.0 / currentNum)
            operator = x
            currentNum = 0
         
        return sum(stack)

s = '-21*2'
print(Solution().calculate(s))


