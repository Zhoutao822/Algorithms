#
# @lc app=leetcode.cn id=380 lang=python
#
# [380] 常数时间插入、删除和获取随机元素
#
# https://leetcode-cn.com/problems/insert-delete-getrandom-o1/description/
#
# algorithms
# Medium (41.32%)
# Total Accepted:    1.9K
# Total Submissions: 4.5K
# Testcase Example:  '["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]\n[[],[1],[2],[2],[],[1],[2],[]]'
#
# 设计一个支持在平均 时间复杂度 O(1) 下，执行以下操作的数据结构。
# 
# 
# insert(val)：当元素 val 不存在时，向集合中插入该项。
# remove(val)：元素 val 存在时，从集合中移除该项。
# getRandom：随机返回现有集合中的一项。每个元素应该有相同的概率被返回。
# 
# 
# 示例 :
# 
# 
# // 初始化一个空的集合。
# RandomizedSet randomSet = new RandomizedSet();
# 
# // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
# randomSet.insert(1);
# 
# // 返回 false ，表示集合中不存在 2 。
# randomSet.remove(2);
# 
# // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
# randomSet.insert(2);
# 
# // getRandom 应随机返回 1 或 2 。
# randomSet.getRandom();
# 
# // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
# randomSet.remove(1);
# 
# // 2 已在集合中，所以返回 false 。
# randomSet.insert(2);
# 
# // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。
# randomSet.getRandom();
# 
# 
#
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mymap = dict()
        self.mylist = list()
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.mymap:
            return False
        else:
            self.mylist.insert(self.size, val)
            self.mymap[val] = self.size
            self.size += 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.mymap:
            return False
        else:
            oldIndex = self.mymap[val];
            lastVal = self.mylist[self.size - 1];
            self.mylist[oldIndex] = lastVal;
            self.mymap[lastVal] = oldIndex;
            self.mymap.pop(val)
            self.size -= 1;
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return self.mylist[random.randint(0, self.size - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

