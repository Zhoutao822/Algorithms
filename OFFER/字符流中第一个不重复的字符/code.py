# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    # 请实现一个函数用来找出字符流中第一个只出现一次的字符。
    # 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
    # 当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
    def __init__(self):
        self.stack = []
        self.map = {}

    def FirstAppearingOnce(self):
        # write code here
        if not self.stack:
            return '#'
        return self.stack[0]

    def Insert(self, char):
        # write code here
        self.map[char] = 1 if char not in self.map else self.map[char] + 1
        if self.map[char] == 1:
            self.stack.append(char)
        elif char in self.stack:
            self.stack.remove(char)