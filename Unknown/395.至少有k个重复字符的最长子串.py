#
# @lc app=leetcode.cn id=395 lang=python
#
# [395] 至少有K个重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (33.57%)
# Total Accepted:    1.2K
# Total Submissions: 3.5K
# Testcase Example:  '"aaabb"\n3'
#
# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
# 
# 示例 1:
# 
# 
# 输入:
# s = "aaabb", k = 3
# 
# 输出:
# 3
# 
# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。
# 
# 
# 示例 2:
# 
# 
# 输入:
# s = "ababbc", k = 2
# 
# 输出:
# 5
# 
# 最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
# 
# 
#
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.helper(s, k, 0, len(s)-1)

    def helper(self, s, k, l, r):
        if l > r:
            return 0
        map = {}
        for i in range(l, r+1):
            map[s[i]] = 1 if s[i] not in map else map[s[i]] + 1
        while l <= r and map[s[l]] < k:
            map[s[l]] -= 1
            l += 1
        while l <= r and map[s[r]] < k:
            map[s[r]] -= 1            
            r -= 1
        for i in range(l+1, r):
            if map[s[i]] < k:
                return max(self.helper(s, k, l, i-1), self.helper(s, k, i+1, r))
        return r - l + 1
        

        # better
        # if len(s) < k: 
        #     return 0 
        # for c in set(s): 
        #     if s.count(c) < k: 
        #         return max(self.longestSubstring(t, k) for t in s.split(c)) 
        # return len(s)
s = 'ababacb'
k = 3
print(Solution().longestSubstring(s, k))
