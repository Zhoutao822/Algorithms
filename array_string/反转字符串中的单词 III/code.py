class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        return ' '.join([c[::-1] for c in s])

s = "Let's take LeetCode contest"

print(Solution().reverseWords(s))