# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ', '%20')

s = 'aa aa  aaa '
print(Solution().replaceSpace(s))