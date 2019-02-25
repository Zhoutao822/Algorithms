class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret = []
        if not strs:
            return ""
        if "" in strs:
            return ""
        str1 = strs[0]        
        if len(strs) == 1:
            return str1
        for i in range(len(str1)):
            for s in strs:
                s = list(s)
                if i >= len(s) or s[i] != str1[i]:
                    return ''.join(ret)
            ret.append(str1[i])
        return ''.join(ret)


# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs: return ""
#         if len(strs) == 1: return strs[0]
        
#         strs.sort()
#         p = ''
#         for x, y in zip(strs[0], strs[-1]):
#             if x == y:
#                 p += x
#             else:
#                 break
#         return p


s = ["dog","racecar","car"]

print(Solution().longestCommonPrefix(s))