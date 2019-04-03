# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) < 5:
            return False
        zero_count = numbers.count(0)
        numbers.sort()
        start = numbers[zero_count]
        arr = list(range(start, start+5))
        for num in numbers[zero_count:]:
            if num in arr:
                arr.remove(num)
        return zero_count == len(arr)

n = [1,3,2,6,4]
print(Solution().IsContinuous(n))
