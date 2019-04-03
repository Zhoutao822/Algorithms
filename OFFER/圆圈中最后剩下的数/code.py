# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        # 约瑟夫环问题
        # f(n,m) = (f(n-1, m) + m) % n
        if n == 0:
            return -1
        p = 0
        for i in range(2, n+1):
            p = (p + m) % i
        return p+1

n = 11
m = 3
print(Solution().LastRemaining_Solution(n, m))