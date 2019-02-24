class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join([str(c) for c in digits]))
        num += 1
        return [int(c) for c in list(str(num))]


n = [1,2,3,4]
print(Solution().plusOne(n))