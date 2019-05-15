#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 朋友圈
#
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        assert len(M) == len(M[0])
        l = len(M)

        visited = set()

        def dfs(i):
            for j in range(l):
                if M[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        
        count = 0
        for i in range(l):
            if i not in visited:
                dfs(i)
                count += 1
        return count

m = [
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
print(Solution().findCircleNum(m))