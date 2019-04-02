# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        # 一个整型数组里除了两个数字之外，其他的数字都出现了两次。
        # 请写程序找出这两个只出现一次的数字。
        # map = {}
        # res = []
        # for num in array:
        #     map[num] = 1 if num not in map else map[num] + 1
        # for key, val in map.items():
        #     if val == 1:
        #         res.append(key)
        # assert len(res) == 2
        # return res
        # 异或运算，将数组一分为二
        s = 0
        for num in array:
            s ^= num
        index = 0
        while s & 1 != 1:
            index += 1
            s = s >> 1
        def helper(num):
            num = num >> index
            return num & 1
        a, b = 0, 0
        for num in array:
            if helper(num):
                a ^= num
            else:
                b ^= num
        return [a, b]

n = [1,2,3,4,3,1]
print(Solution().FindNumsAppearOnce(n))