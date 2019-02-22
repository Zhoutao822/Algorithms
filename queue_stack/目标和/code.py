class Solution:
    def findTargetSumWays(self, nums: 'List[int]', S: 'int') -> 'int':
        """
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/219/stack-and-dfs/885/
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        def dfs(i, s):
            count = 0
            if i == len(nums):
                return 1 if s - S == 0 else 0

            count += dfs(i + 1, s - nums[i])
            count += dfs(i + 1, s + nums[i])
            return count
        return dfs(0, 0)
nums = [6,44,30,25,8,26,34,22,10,18,34,8,0,32,13,48,29,41,16,30]

S = 12
print(Solution().findTargetSumWays(nums, S))
