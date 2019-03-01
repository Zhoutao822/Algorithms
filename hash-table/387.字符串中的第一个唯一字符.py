#
# @lc app=leetcode.cn id=387 lang=python
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode-cn.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (35.74%)
# Total Accepted:    21.1K
# Total Submissions: 58.9K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 案例:
# 
# 
# s = "leetcode"
# 返回 0.
# 
# s = "loveleetcode",
# 返回 2.
# 
# 
# 
# 
# 注意事项：您可以假定该字符串只包含小写字母。
# 
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = dict()
        for _, v in enumerate(s):
            if v not in map.keys():
                map[v] = 1
            else:
                map[v] += 1
        char_list = [c for c in map.keys() if map[c] == 1]
        for k, v in enumerate(s):
            if v in char_list:
                return k
        return -1
