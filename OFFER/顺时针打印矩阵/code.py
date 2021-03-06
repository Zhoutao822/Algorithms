# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        # 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
        # 例如，如果输入如下4 X 4矩阵： 
        # 1  2  3  4 
        # 5  6  7  8 
        # 9  10 11 12 
        # 13 14 15 16 
        # 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            return [matrix[0][0]]
        ret = []
        i = 0
        while m > 0 and n > 0:
            if m == 1:
                for j in range(n):
                    ret.append(matrix[i][i+j])
                break
            if n == 1:
                for j in range(m):
                    ret.append(matrix[i+j][i])
                break
            for j in range(n-1):
                ret.append(matrix[i][i+j])
            for j in range(m-1):
                ret.append(matrix[i+j][i+n-1])
            for j in range(n-1, 0, -1):
                ret.append(matrix[i+m-1][i+j])
            for j in range(m-1, 0, -1):
                ret.append(matrix[i+j][i])
            i += 1
            m -= 2
            n -= 2
        return ret
m = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
a = [[1]]
print(Solution().printMatrix(a))
# print(m[0][3])
