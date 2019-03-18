# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        # 与斐波那契一样
        if number == 0: return 0
        if number == 1: return 1
        if number == 2: return 2
        self.arr = [0, 1, 2]
        for i in range(3, number+1):
            self.arr.append(self.arr[i-1] + self.arr[i-2])
        return self.arr[number]