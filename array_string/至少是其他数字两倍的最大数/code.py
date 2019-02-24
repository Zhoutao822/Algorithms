class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        index = nums.index(max_num)
        nums.remove(max_num)
        for num in nums:
            if num * 2 > max_num:
                return -1
        return index

n = [1, 2, 3, 4]

print(Solution().dominantIndex(n))