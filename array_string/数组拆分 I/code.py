class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum
        # return sum(sorted(nums)[::2])

s = [1,3,2,4]  

print(Solution().arrayPairSum(s))