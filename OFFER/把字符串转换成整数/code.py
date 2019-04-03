# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        # 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
        # 要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
        if not s:
            return 0
        if s[0] == '+':
            return self.parseInt(s, 1, True)
        elif s[0] == '-':
            return self.parseInt(s, 1, False)
        elif s[0].isdigit():
            return self.parseInt(s, 0, True)
        else:
            return 0


    def parseInt(self, s, index, flag):
        if index > len(s)-1:
            return 0
        ret = 0
        while index < len(s) and s[index].isdigit():
            ret = ret * 10 + int(s[index])
            index += 1
        if index != len(s):
            return 0
        return ret if flag else -ret

s = '123'
print(Solution().StrToInt(s))