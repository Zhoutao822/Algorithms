# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        # 递归肯定是不可以的，因为两项之间重复计算，使用动态规划DP，保存计算过程中的值
        self.arr = [0, 1]
        if n == 0: return 0
        if n == 1: return 1
        for i in range(2,n+1):
            self.arr.append(self.arr[i-1] + self.arr[i-2])
        return self.arr[n]

print(Solution().Fibonacci(39))