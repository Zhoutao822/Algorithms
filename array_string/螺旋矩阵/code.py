class Solution(object):
    def spiralOrder(self, matrix):
        """
        url: https://leetcode-cn.com/explore/learn/card/array-and-string/199/introduction-to-2d-array/775/
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])

        cycle = min([round(float(m) / 2), round(float(n) / 2)])
        ret = []
        for i in range(int(cycle)):
            if m == n == 1:
                ret.append(matrix[i][i])
                break
            if m == 1:
                for k in range(n):
                    ret.append(matrix[i][i + k])
                break
            if n == 1:
                for k in range(m):
                    ret.append(matrix[i + k][i])
                break
            for k in range(n - 1):
                ret.append(matrix[i][i + k])

            for k in range(m - 1):
                ret.append(matrix[i + k][i + n - 1])

            for k in range(n - 1):
                ret.append(matrix[i + m - 1][i + n - k - 1])

            for k in range(m - 1):
                ret.append(matrix[i + m - k - 1][i])
            m -= 2
            n -= 2
        return ret

m = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

print(Solution().spiralOrder(m))