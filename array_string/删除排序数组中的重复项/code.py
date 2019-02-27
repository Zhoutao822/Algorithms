class Solution(object):
    def removeDuplicates(self, nums):
        """
        url: https://leetcode-cn.com/explore/learn/card/array-and-string/202/conclusion/795/
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        j = 0
        while j < len(nums) - 1:
            j += 1
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

n  = [1,1,2]

print(Solution().removeDuplicates(n))
print(n)