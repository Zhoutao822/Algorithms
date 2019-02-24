class Solution(object):
    def pivotIndex(self, nums):
        """
        url: https://leetcode-cn.com/explore/learn/card/array-and-string/198/introduction-to-array/770/
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 3: return -1
        s = sum(nums)
        tmp = 0
        for i in range(length):
            if tmp * 2 + nums[i] == s:
                return i
            else:
                tmp += nums[i]
        return -1

n = [-1,-1,-1,0,1,1]
print(Solution().pivotIndex(n))

