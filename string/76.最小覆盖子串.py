#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ls = len(s)
        lt = len(t)
        min_len = ls + 1
        if not s or not t or ls < lt:
            return ''
        map = {}
        for c in t:
            map[c] = map.get(c, 0) + 1
        match = 0
        l, r = 0, 0
        start, end = 0, ls - 1
        while r < ls:
            map[s[r]] = map.get(s[r], 0) - 1
            match = match + 1 if map[s[r]] >= 0 else match
            if match == lt:
                while map[s[l]] < 0:
                    map[s[l]] += 1
                    l += 1
                if min_len > r - l + 1:
                    min_len = r - l + 1
                    start = l
                    end = r
            r += 1
        return '' if min_len > ls else s[start : end + 1]

