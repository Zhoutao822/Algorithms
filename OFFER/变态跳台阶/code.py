# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 0: return 0
        if number == 1: return 1
        if number == 2: return 2
        self.arr = [0,1,2]
        for _ in range(3, number + 1):
            self.arr.append(sum(self.arr) + 1)
        return self.arr[number]
        # 累加和，better
        # return 1 << (number-1)