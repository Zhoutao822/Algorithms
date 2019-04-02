# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        # 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
        # res = []
        # def getArr(start, count):
        #     return [int(start+i) for i in range(count)]

        # import math
        # max_count = int(math.sqrt(2 * tsum))
        # for count in range(max_count, 1, -1):
        #     tmp = 2 * tsum - count ** 2 + count
        #     if tmp % (2 * count) == 0:
        #         res.append(getArr(tmp / (2*count), count))
        # return res

        if tsum < 3:
            return []
        ret = []
        low = 1
        high = 2
        curSum = low + high
        mid = (tsum + 1) >> 1
        while low < mid:
            if curSum == tsum:
                ret.append(list(range(low, high+1)))
                high += 1
                curSum += high
            elif curSum < tsum:
                high += 1
                curSum += high
            else:
                curSum -= low
                low += 1
        return ret    



s = 100
print(Solution().FindContinuousSequence(s))