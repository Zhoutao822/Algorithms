#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (38.66%)
# Total Accepted:    6.2K
# Total Submissions: 15.8K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 动态规划
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[len(s)]
        
        # 另一种
        # if not s:
        #     return True
        
        # breakp = [0]
        
        # for i in range(len(s) + 1):
        #     for j in breakp:
        #         if s[j:i] in wordDict:
        #             breakp.append(i)
        #             break
        # return breakp[-1] == len(s)
        
s = "goalspecial"
wordDict = ["go","goal","goals","special"]
print(Solution().wordBreak(s, wordDict))
