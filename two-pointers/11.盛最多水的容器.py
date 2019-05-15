#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        l, r = 0, len(height)-1
        while l < r:
            maxArea = max(maxArea, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1 
        return maxArea
