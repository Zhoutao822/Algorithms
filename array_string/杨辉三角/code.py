class Solution(object):
    def generate(self, numRows):
        """
        url: https://leetcode-cn.com/explore/learn/card/array-and-string/199/introduction-to-2d-array/776/
        :type numRows: int
        :rtype: List[List[int]]
        """
        row1 = [1]
        row2 = [1, 1]
        if numRows == 0:
            return []
        if numRows == 1:
            return [row1]
        if numRows == 2:
            return [row1, row2]
        ret = [row1, row2]
        for i in range(3, numRows + 1):
            row = [1] * i
            last_row = ret[i - 2]
            for j in range(1, i - 1):
                row[j] = last_row[j - 1] + last_row[j]
            ret.append(row)
        return ret

    def generate_(self, numRows):
        """
        url: https://leetcode-cn.com/explore/learn/card/array-and-string/199/introduction-to-2d-array/776/
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            now = [1] * (i + 1)
            if i >= 2:
                for j in range(1, i):
                    now[j] = pre[j - 1] + pre[j]
            result.append(now)
            pre = now
        return result

print(Solution().generate_(5))