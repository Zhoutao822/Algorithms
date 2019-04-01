#
# @lc app=leetcode.cn id=341 lang=python
#
# [341] 扁平化嵌套列表迭代器
#
# https://leetcode-cn.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (53.72%)
# Total Accepted:    1.2K
# Total Submissions: 2.1K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# 给定一个嵌套的整型列表。设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
# 
# 列表中的项或者为一个整数，或者是另一个列表。
# 
# 示例 1:
# 
# 输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
# 
# 示例 2:
# 
# 输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回false，next 返回的元素的顺序应该是: [1,4,6]。
# 
# 
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        def helper(li):
            for n in li:
                if n.isInteger():
                    self.stack.append(n)
                else:
                    helper(n.getList())
        helper(nestedList)
        self.stack = self.stack[::-1]

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

