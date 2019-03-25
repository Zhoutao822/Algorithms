#
# @lc app=leetcode.cn id=140 lang=python
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (33.58%)
# Total Accepted:    2.3K
# Total Submissions: 6.6K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
# 
# 说明：
# 
# 
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# 示例 2：
# 
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
# 
# 
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        stride = [len(word) for word in wordDict]
        stride_set = set(stride)
        # max_stride = max(stride)
        res = []
        if self.canBreak(s, wordDict):
            self.subBreak(s, wordDict, stride_set, [], res)
        return res
    
    def subBreak(self, s, wordDict, stride, cur_result, res):
        if len(s) == 0:
            res.append(' '.join(cur_result))
        else:
            for stride_length in stride:
                if stride_length <= len(s):
                    if s[:stride_length] in wordDict:
                        self.subBreak(s[stride_length:], wordDict, stride, cur_result + [s[:stride_length]], res)

    def canBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]

