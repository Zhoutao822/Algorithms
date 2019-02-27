class Solution(object):
    def reverseWords(self, s):
        """
        url: https://leetcode-cn.com/explore/learn/card/array-and-string/202/conclusion/793/
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))

s = '  a   qwe   qqq '


print(Solution().reverseWords(s))



