# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        # 统计一个数字在排序数组中出现的次数。
        # return data.count(k)
        # 二分查找，高位index - 低位index，这里没说顺序，所以需要考虑
        return self.binarySearch(data, k+0.5) - self.binarySearch(data, k-0.5)

    def binarySearch(self, data, k):
        s = 0
        e = len(data) - 1
        while s <= e:
            mid = (s + e) // 2
            if data[mid] > k:
                e = mid -1 
            elif data[mid] < k:
                s = mid + 1
        return s