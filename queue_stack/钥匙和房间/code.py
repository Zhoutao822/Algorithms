class Solution:
    def canVisitAllRooms(self, rooms):
        """
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/220/conclusion/893/
        """

        N = len(rooms)
        visited = set()
        visited.add(0)

        def dfs(i):
            if not rooms[i]:
                return
            for n in rooms[i]:
                if n not in visited:
                    visited.add(n)
                    dfs(n)

        dfs(0)
        if len(visited) != N:
            return False
        else:
            return True

r = [[1,3],[3,0,1],[2],[0]]

print(Solution().canVisitAllRooms(r))