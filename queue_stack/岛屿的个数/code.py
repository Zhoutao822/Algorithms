class Solution:
    def numIslands(self, grid):
        """BFS
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/217/queue-and-bfs/872/
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid is None or len(grid) == 0:
            return 0
        max_rows = len(grid)
        max_columns = len(grid[0])
        count = 0
        queue = []
        used_queue = set()
        land_coordinates = [(x, y) for x in range(max_rows) for y in range(max_columns) if grid[x][y] is "1"]
        
        def getNeighbors(x, y, max_rows, max_columns):
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            return [
                coo for coo in neighbors 
                if coo[0] not in [-1, max_rows] and coo[1] not in [-1, max_columns]]

        
        for coordinate in land_coordinates:
            if coordinate in used_queue:
                continue
            queue.append(coordinate)
            used_queue.add(coordinate)
            count += 1
            while len(queue) > 0:
                size = len(queue)
                for _ in range(size):
                    for neighbor in getNeighbors(queue[0][0], queue[0][1], max_rows, max_columns):
                        if neighbor not in used_queue:
                            if grid[neighbor[0]][neighbor[1]] is "1":
                                queue.append(neighbor)
                                used_queue.add(neighbor)
                    queue.pop(0)
        return count

    def numIslands_dfs(self, grid):
        """DFS
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        r = len(grid)
        c = len(grid[0])
        count = 0

        def dfs(x, y, r, c):
            grid[x][y] = "0"
            if x != 0 and grid[x - 1][y] is "1":
                dfs(x - 1, y, r, c)
            if x != r -1 and grid[x + 1][y] is "1":
                dfs(x + 1, y, r, c)
            if y != 0 and grid[x][y - 1] is "1":
                dfs(x, y - 1, r, c)
            if y != c -1 and grid[x][y + 1] is "1":
                dfs(x, y + 1, r, c)
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] is "1":
                    count += 1
                    dfs(i, j, r, c)
        return count

s = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

print(s.numIslands_dfs(grid))