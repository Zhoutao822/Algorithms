#
# @lc app=leetcode.cn id=658 lang=python
#
# [658] 找到 K 个最接近的元素
#
# https://leetcode-cn.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (36.51%)
# Total Accepted:    1.2K
# Total Submissions: 3.2K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x
# 的差值一样，优先选择数值较小的那个数。
# 
# 示例 1:
# 
# 
# 输入: [1,2,3,4,5], k=4, x=3
# 输出: [1,2,3,4]
# 
# 
# 
# 
# 示例 2:
# 
# 
# 输入: [1,2,3,4,5], k=4, x=-1
# 输出: [1,2,3,4]
# 
# 
# 
# 
# 说明:
# 
# 
# k 的值为正数，且总是小于给定排序数组的长度。
# 数组不为空，且长度不超过 10^4
# 数组里的每个元素与 x 的绝对值不超过 10^4
# 
# 
# 
# 
# 更新(2017/9/19):
# 这个参数 arr 已经被改变为一个整数数组（而不是整数列表）。 请重新加载代码定义以获取最新更改。
# 
#
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        while len(arr) > k:
            if abs(x - arr[0]) > abs(x - arr[-1]):
                arr = arr[1:]
            else:
                arr = arr[:-1]
        return arr

        # better
        # left = 0
        # right = len(arr)-k
        # while left < right:
        #     mid = left + (-left+right)//2
        #     if abs(arr[mid]-x)>abs(arr[mid+k]-x):
        #         left = mid + 1
        #     else:
        #         right = mid

        # return arr[left:left+k]
