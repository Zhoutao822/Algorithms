# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        # 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
        # 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
        if not ss: return []
        ret = list()
        self.helper(ss, ret, '')
        return sorted(list(set(ret)))

    def helper(self, s, ret, path):
        if s == '':
            ret.append(path)
        else:
            for i in range(len(s)):
                self.helper(s[:i] + s[i+1:], ret, path + s[i])