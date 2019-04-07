# -*- coding:utf-8 -*-
class Solution:
    # 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
    # 那么中位数就是所有数值排序之后位于中间的数值。
    # 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
    # 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
    def __init__(self):
        self.sorted_list = []

    def Insert(self, num):
        # write code here
        if not self.sorted_list:
            self.sorted_list.append(num)
        else:
            index = self.BinarySearch(self.sorted_list, num)
            self.sorted_list.insert(index, num)

    def GetMedian(self, nums):
        # write code here
        index = len(self.sorted_list) // 2
        if len(self.sorted_list) % 2 == 1:
            return self.sorted_list[index]
        else:
            return (self.sorted_list[index-1] + self.sorted_list[index]) / 2.

    def BinarySearch(self, nums, num):
        l, h = 0, len(nums)-1
        if num > nums[-1]:
            return len(nums)
        if num < nums[0]:
            return 0
        while l < h:
            mid = (l + h) // 2
            if nums[mid] < num:
                l = mid + 1
            else:
                h = mid
        return l
