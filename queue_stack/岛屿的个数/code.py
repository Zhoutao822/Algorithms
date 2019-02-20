class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return None

    def getNeighbors(self, x, y, max_rows, max_columns):
        neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        for n in neighbors:
            if n[0] in [-1, max_rows]:
                neighbors.remove(n)
            if n[1] in [-1, max_columns]:
                neighbors.remove(n)
        return neighbors
