class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1
        return

n = [2, 7, 11, 15]
t = 9
print(Solution().twoSum(n, t))        