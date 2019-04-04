# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        # 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
        # 例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
        # 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
        flag = False
        demical = False
        hasE = False
        for i in range(len(s)):
            if s[i] in ['e', 'E']:
                if i == len(s) - 1: return False
                if hasE: return False
                hasE = True
            elif s[i] in ['+', '-']:
                if flag and s[i-1] not in ['e', 'E']: return False
                if not flag and i > 0 and s[i-1] not in ['e', 'E']: return False
                flag = True
            elif s[i] == '.':
                if hasE or demical:
                    return False
                demical = True
            elif not s[i].isdigit():
                return False
        return True

