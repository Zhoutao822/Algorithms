import time
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        return base ** exponent

        # n = abs(exponent)
        # result = 1
        # while n != 0:
        #     if (n & 1) == 1:
        #         result *= base
        #     base *= base
        #     n >>= 1
        # return result if exponent > 0 else 1 / result

start = time.clock()
print(Solution().Power(5.31, 200))
stop = time.clock()
print(stop - start)
