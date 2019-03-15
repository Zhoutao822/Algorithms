# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
            if target in array[i]:
                return True
        return False

t = 15
n = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print(Solution().Find(t, n))