class Solution(object):
    def smallestRepunitDivByK(self, K):
        """ 给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小的正整数 N。
            返回 N 的长度。如果不存在这样的 N，就返回 -1。
        :type K: int
        :rtype: int
        """
        N = 1
        count = 1
        try:
            while True:
                if N % K == 0:
                    return count
                else:
                    N = 10 * N + 1
                    count += 1
        except:
            return -1

k = 4
print(Solution().smallestRepunitDivByK(k))