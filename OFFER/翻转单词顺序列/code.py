# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        # “student. a am I” => “I am a student.”
        s = s.split(' ')
        return ' '.join(s[::-1])
s = ' 12  3 4  '
print(Solution().ReverseSentence(s))