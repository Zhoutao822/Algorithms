class Solution(object):
    def rotate(self, nums, k):
        """
        url: https://leetcode-cn.com/explore/learn/card/array-and-string/202/conclusion/791/
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # if k == 0:
        #     return nums
        # for _ in range(k):
        #     tmp = nums[-1]
        #     for i in range(len(nums) - 1, 0, -1):
        #         nums[i] = nums[i-1]
        #     nums[0] = tmp
        # return nums

        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums

n = [1,2,3,4,5,6,7]
k = 3
print(Solution().rotate(n, k))