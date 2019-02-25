class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        try:
            return haystack.index(needle)
        except:
            return -1


haystack = "hello"
needle = "llq"

print(Solution().strStr(haystack, needle))