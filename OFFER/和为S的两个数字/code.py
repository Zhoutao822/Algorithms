# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        # 输入一个递增排序的数组和一个数字S，在数组中查找两个数，
        # 使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
        i, j = 0, len(array)-1
        while i < j:
            curSum = array[i] + array[j]
            if curSum == tsum:
                return [array[i], array[j]]
            elif curSum > tsum:
                j -= 1
            else:
                i += 1
        return []