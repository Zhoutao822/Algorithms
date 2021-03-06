#
# @lc app=leetcode.cn id=128 lang=python
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (41.39%)
# Total Accepted:    6.3K
# Total Submissions: 14.7K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 
# 要求算法的时间复杂度为 O(n)。
# 
# 示例:
# 
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
#
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {}
        max_length = 0
        for num in nums:
            if num not in map:
                left = map.get(num-1, 0)
                right = map.get(num+1, 0)

                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length
                map[num] = cur_length
                map[num-left] = cur_length
                map[num+right] = cur_length
        return max_length

