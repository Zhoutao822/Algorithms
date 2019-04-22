#
# @lc app=leetcode.cn id=149 lang=python
#
# [149] 直线上最多的点数
#
# https://leetcode-cn.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (14.88%)
# Total Accepted:    2.4K
# Total Submissions: 14.6K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
# 
# 示例 1:
# 
# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 
# 
# 示例 2:
# 
# 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# 
#
# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import random

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def getLine(p1, p2):
            a = p2.y - p1.y
            b = p1.x - p2.x
            c = p2.x*p1.y - p1.x*p2.y
            return (a, b, c)
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        maxPoint = 0
        ran = list()
        # 利用随机数取点，不需要遍历所有直线，但是仅限于样本点数较少的情况
        for _ in range(100):
            tmp = random.sample(points, 2)
            ran.append(tmp)
        for pointComb in ran:
            line = getLine(pointComb[0], pointComb[1])
            a = line[0]; b = line[1]; c = line[2]
            p1 = pointComb[0]; p2 = pointComb[1]
            tmp = 0
            for p in points:
                if (a*p.x + b*p.y + c == 0 and (not (p1.x == p2.x and p1.y == p2.y))) or (p.x == p1.x == p2.x and p.y == p1.y == p2.y):
                    tmp += 1
            if (tmp > maxPoint):
                maxPoint = tmp
        return maxPoint
        

