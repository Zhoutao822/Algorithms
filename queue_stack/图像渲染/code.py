class Solution:
    def floodFill(self, image: 'List[List[int]]', sr: 'int', sc: 'int', newColor: 'int') -> 'List[List[int]]':
        """
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/220/conclusion/891/
        """
        visited = set()
        row = len(image)
        column = len(image[0])
        color = image[sr][sc]
        def dfs(x, y):
            image[x][y] = newColor
            visited.add((x, y))
            if x != 0 and image[x - 1][y] == color and (x-1, y) not in visited: dfs(x-1, y)
            if x != row - 1 and image[x + 1][y] == color and (x+1, y) not in visited: dfs(x+1, y)
            if y != 0 and image[x][y - 1] == color and (x, y-1) not in visited: dfs(x, y-1)
            if y != column - 1 and image[x][y + 1] == color and (x, y+1) not in visited: dfs(x, y+1)
        dfs(sr, sc)
        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

print(Solution().floodFill(image, sr,sc, newColor))