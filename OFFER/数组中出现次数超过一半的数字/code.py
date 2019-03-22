# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        # 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
        # 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
        # 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
        # 如果不存在则输出0。

        target = None
        count = 0
        for num in numbers:
            if count == 0:
                target = num
                count += 1
            else:
                if target != num:
                    count -= 1
                else:
                    count += 1
        # 验证
        count = 0
        for num in numbers:
            if num == target: count += 1
        if count * 2 > len(numbers): return target
        else: return 0
                
n = [1,2,3,2,4,2,5,2,3]
print(Solution().MoreThanHalfNum_Solution(n))