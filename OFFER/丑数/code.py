# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
        # 例如6、8都是丑数，但14不是，因为它包含质因子7。 
        # 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
        if index == 0: return 0
        res = [1] * index
        i, j, k = 0, 0, 0
        for m in range(1, index):
            res[m] = min([res[i] * 2, res[j] * 3, res[k] * 5])
            if res[m] == res[i] * 2: i += 1
            if res[m] == res[j] * 3: j += 1
            if res[m] == res[k] * 5: k += 1
        return res[index-1]
