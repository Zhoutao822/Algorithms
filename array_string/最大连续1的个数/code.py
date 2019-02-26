class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # if not nums or 1 not in nums:
        #     return 0
        # ret = 0
        # flag = True
        # j = 0
        # for i in range(len(nums)):
        #     if flag and nums[i] == 1:
        #         j = i
        #         flag = False
        #     elif not flag and nums[i] == 0:
        #         ret = max([ret, i - j])
        #         flag = True
        #     if not flag and i == len(nums) - 1:
        #         ret = max([ret, i - j + 1])
        # return ret


        ret = 0
        _sum = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                _sum += 1
            else:
                if ret < _sum:
                    ret = _sum
                _sum = 0
        return max([ret, _sum])