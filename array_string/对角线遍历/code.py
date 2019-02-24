class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        url: https://leetcode-cn.com/explore/learn/card/array-and-string/199/introduction-to-2d-array/774/
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        M = len(matrix) - 1
        N = len(matrix[0]) - 1
        ret = []
        for i in range(M + N + 1):
            a = 0 if i < N else i - N
            b = M if i > M else i
            if i % 2 == 1:
                for x in range(a, b + 1):
                    ret.append(matrix[x][i - x])
            else:
                for x in range(b, a - 1, -1):                
                    ret.append(matrix[x][i - x])
        return ret

n = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print(Solution().findDiagonalOrder(n))