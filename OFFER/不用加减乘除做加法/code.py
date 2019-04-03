# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        # 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
        # 位运算
        while num2 != 0:
            tmp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = tmp
        return num1
n1 = 40
n2 = 156
print(Solution().Add(n1,n2))