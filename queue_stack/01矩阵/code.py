# class Solution:
#     def updateMatrix(self, matrix):
#         """
#         url: https://leetcode-cn.com/explore/learn/card/queue-stack/220/conclusion/892/
#         """
#         row = len(matrix)
#         column = len(matrix[0])
#         visited = set()

#         def dfs(x, y, row, column):
#             if (x, y) in visited:
#                 return matrix[x][y]
#             if x not in range(row) or y not in range(column):
#                 return float('inf')
#             if matrix[x][y] == 0:
#                 return 0
#             visited.add((x, y))
#             if x != 0 and matrix[x - 1][y] == 0:
#                 matrix[x][y] = 1
#                 return 1
#             if x != row - 1 and matrix[x + 1][y] == 0:
#                 matrix[x][y] = 1
#                 return 1
#             if y != 0 and matrix[x][y - 1] == 0:
#                 matrix[x][y] = 1
#                 return 1
#             if y != column - 1 and matrix[x][y + 1] == 0:
#                 matrix[x][y] = 1
#                 return 1
#             best_step = min([
#                 dfs(x - 1, y, row, column),
#                 dfs(x + 1, y, row, column),
#                 dfs(x, y - 1, row, column),
#                 dfs(x, y + 1, row, column)
#             ]) + 1
#             matrix[x][y] = best_step
#             return best_step

#         for i in range(row):
#             for j in range(column):
#                 if matrix[i][j] != 0:
#                     dfs(i, j, row, column)
#         return matrix

class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        Q = []
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    Q.append((i, j))
                    visited.add((i, j))
        
        while Q:
            i, j = Q.pop(0)
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    matrix[x][y] = matrix[i][j] + 1
                    visited.add((x, y))
                    Q.append((x, y))
        return matrix

m = [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], 
     [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
     [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], 
     [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
     [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], 
     [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
     [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], 
     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
     [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], 
     [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]

print(Solution().updateMatrix(m))
