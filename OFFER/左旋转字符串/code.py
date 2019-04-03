# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        # 对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
        # 例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
        # if not s:
        #     return s
        # n = n % len(s)
        # return s[n:] + s[:n]
        
        # swap
        if not s:
            return s
        n = n % len(s)
        first = list(s[:n])
        second = list(s[n:])
        first = first[::-1]
        second = second[::-1]
        first.extend(second)
        return ''.join(first[::-1])
    


s = '12345'
n = 8
print(Solution().LeftRotateString(s, n))