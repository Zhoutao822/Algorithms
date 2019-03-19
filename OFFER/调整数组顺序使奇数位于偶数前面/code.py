# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        # 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
        # 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
        # 并保证奇数和奇数，偶数和偶数之间的相对位置不变。
        # 1.要想保证原有次序，则只能顺次移动或相邻交换。
        # 2.i从左向右遍历，找到第一个偶数。
        # 3.j从i+1开始向后找，直到找到第一个奇数。
        # 4.将[i,...,j-1]的元素整体后移一位，最后将找到的奇数放入i位置，然后i++。
        # 5.終止條件：j向後遍歷查找失敗。
        if not array or len(array) == 1:
            return array
        for i in range(len(array)):
            if array[i] % 2 == 0:
                if i+1 > len(array):
                    break
                for j in range(i+1, len(array)):
                    if array[j] % 2 == 1:
                        tmp = array[j]
                        array[i+1:j+1] = array[i:j]
                        array[i] = tmp
                        break
        return array
        
n = [1,2,3,4,5,6,7]
Solution().reOrderArray(n)
print(n)