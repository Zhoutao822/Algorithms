class Solution:
    def openLock(self, deadends, target):
        """
        BFS
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/217/queue-and-bfs/873/
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        step = -1
        lock = "0000"
        if lock in deadends:
            return -1
        if target == lock:
            return 0
        queue = []
        used_queue = set()
        def getNextLocks(cur_lock, deadends):
            tmp_list = []
            for i in range(len(cur_lock)):
                for t in [-1, 1]:
                    tmp_lock = list(cur_lock)
                    tmp_lock[i] = str((int(tmp_lock[i]) + t) % 10)
                    tmp_list.append("".join(tmp_lock))
            return [next_lock for next_lock in tmp_list if next_lock not in deadends]

        queue.append(lock)
        used_queue.add(lock)
        while queue:
            size = len(queue)
            step += 1            
            for _ in range(size):
                cur_lock = queue[0]
                if target == cur_lock:
                    return step
                for next_lock in getNextLocks(cur_lock, deadends):
                    if next_lock not in used_queue:
                        used_queue.add(next_lock)
                        queue.append(next_lock)
                queue.pop(0)
        return -1

    def openLock_plus(self, deadends, target):
        """
        双向BFS
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/217/queue-and-bfs/873/
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        set1 = set(["0000"])
        set2 = set([target])
        visited_set = set(["0000"])
        step = 0

        while set1 and set2:
            if (len(set1) > len(set2)):
                tmp = set1
                set1 = set2
                set2= tmp
            tmp_set = set()
            step += 1
            for lock in set1:
                for i in range(len(lock)):
                    for t in [-1, 1]:
                        next_lock = list(lock)
                        next_lock[i] = str((int(lock[i]) + t) % 10)
                        next_lock = "".join(next_lock)
                        if next_lock in set2:
                            return step
                        if next_lock not in deadends and next_lock not in visited_set:
                            tmp_set.add(next_lock)
                            visited_set.add(next_lock)
            set1 = tmp_set
        return -1




dead = ["0201","0101","0102","1212","2002"]

target = "0202"

s = Solution()

print(s.openLock(dead, target))

