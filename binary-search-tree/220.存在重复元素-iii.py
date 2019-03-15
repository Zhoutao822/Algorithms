#
# @lc app=leetcode.cn id=220 lang=python
#
# [220] 存在重复元素 III
#
# https://leetcode-cn.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (23.02%)
# Total Accepted:    3.3K
# Total Submissions: 14K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j
# 之间的差的绝对值最大为 ķ。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
#
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
#
# 示例 3:
#
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false
#
# 通过将num[i]整除t+1，就可以将距离为t转换为距离为1，再将值存入dict中
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: return False
        hashmap = {}
        for i in range(len(nums)):
            m = nums[i] // (t + 1)
            if m in hashmap:
                return True
            if (m - 1 in hashmap and abs(nums[i] - hashmap[m - 1]) <= t) or (
                    m + 1 in hashmap and abs(nums[i] - hashmap[m + 1]) <= t):
                return True
            hashmap[m] = nums[i]
            if i - k >= 0:
                key = nums[i-k] // (t+1)
                hashmap.pop(key)
        return False
                
