# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray: return 0
        l, r = 0, len(rotateArray) - 1
        while l < r:
            mid = (l + r) // 2
            if rotateArray[mid] < rotateArray[r]:
                r = mid
            else:
                l = mid + 1
        return rotateArray[r]