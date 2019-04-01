#
# @lc app=leetcode.cn id=295 lang=python
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (33.45%)
# Total Accepted:    1.9K
# Total Submissions: 5.3K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
# 
# 例如，
# 
# [2,3,4] 的中位数是 3
# 
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 
# 设计一个支持以下两种操作的数据结构：
# 
# 
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 
# 
# 示例：
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 进阶:
# 
# 
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
# 
# 
# 不适合num范围很大的情况，仅适合100以内
# class MedianFinder(object):

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.map = {}
#         self.length = 0

#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: None
#         """
#         self.map[num] = 1 if num not in self.map else self.map[num] + 1
#         self.length += 1
        
#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         mid = self.length // 2
#         keys = sorted(self.map.keys())
#         for i in range(len(keys)):
#             mid -= self.map[keys[i]]
#             if mid < 0:
#                 return keys[i]
#             elif mid == 0 and self.length % 2 == 0:
#                 return (keys[i] + keys[i+1]) / 2.
        
# 两个堆，最大堆和最小堆， left是最大堆，right是最小堆
import heapq       
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.right = []
        self.left = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num < self.findMedian():
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        if len(self.left) > len(self.right):
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif (len(self.right) - len(self.left)) > 1:
            heapq.heappush(self.left, -heapq.heappop(self.right))


    def findMedian(self):
        """
        :rtype: float
        """
        if not self.left and not self.right:
            return 0
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2.
        else:
            return self.right[0]
# bisect 二分查找插入 
# import bisect

# class MedianFinder(object):

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.data = []
        

#     def addNum(self, num):
#         """
#         :type num: int
#         :rtype: void
#         """
#         bisect.insort(self.data,num)
        

#     def findMedian(self):
#         """
#         :rtype: float
#         """
#         length = len(self.data)
#         if length % 2 == 0:
#             return (self.data[length / 2 - 1] + self.data[length / 2]) / 2.0
#         else:
#             return float(self.data[length // 2])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

