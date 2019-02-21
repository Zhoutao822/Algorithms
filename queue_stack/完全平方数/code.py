import math

class Solution:
    def numSquares(self, n: 'int') -> 'int':
        """
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/217/queue-and-bfs/874/
        """
        queue = []
        visited = set()
        step = 1
        queue.append(0)
        visited.add(0)
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue[0]
                for i in range(1, n):
                    new = cur + i * i
                    if new > n:
                        break
                    elif new == n:
                        return step
                    if new not in visited:
                        visited.add(new)
                        queue.append(new)
                queue.pop(0)
            step += 1
        return 1

    def numSquares_(self, n):
            """
            :type n: int
            :rtype: int
            """
            while n % 4 == 0: 
                n /= 4 
            if n % 8 == 7: 
                return 4 
            a = 0 
            while a**2 <= n: 
                b = int((n - a**2)**0.5) 
                if a**2 + b**2 == n: 
                    return (not not a) + (not not b) 
                a += 1 
            return 3

n = 300
s = Solution()

print(s.numSquares(n))
