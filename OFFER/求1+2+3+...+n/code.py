# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.ret = 0
    def Sum_Solution(self, n):
        # write code here
        # 求1+2+3+...+n，
        # 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
        def cal(n):
            self.ret += n
            n -= 1
            return n > 0 and cal(n)
        cal(n)
        return self.ret

print(Solution().Sum_Solution(10))