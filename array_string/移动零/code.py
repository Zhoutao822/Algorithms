class Solution(object):
    def moveZeroes(self, nums):
        """
        url: https://leetcode-cn.com/explore/learn/card/array-and-string/202/conclusion/796/
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1 or 0 not in nums:
            return
        i = 0
        j = 0
        while True:
            if nums[i] == 0:
                j = i
                break
            i += 1
        while j < len(nums) - 1:
            j += 1
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for k in range(i, len(nums)):
            nums[k] = 0

n = [0,1,0,3,12]

Solution().moveZeroes(n)
print(n)