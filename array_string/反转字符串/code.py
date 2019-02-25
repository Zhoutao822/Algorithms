class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        if not s:
            return []
        i = 0
        j = len(s) - 1
        while i < j:
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp
            i += 1
            j -= 1
        return s

        # return s[::-1]
s = ["h","e","l","l","o"]
print(Solution().reverseString(s))
print(list(reversed(''.join(s))))