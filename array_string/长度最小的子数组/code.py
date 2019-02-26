class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0

        length = len(nums) + 1
        _sum = 0
        r = -1
        l = 0
        while l < len(nums):
            if _sum < s and r + 1 < len(nums):
                r += 1
                _sum += nums[r]
            else:
                _sum -= nums[l]
                l += 1
            if _sum >= s:
                length = min([length, r - l + 1])

        return length

s = 7
n = [2,3,1,2,4,3]


print(Solution().minSubArrayLen(s, n))