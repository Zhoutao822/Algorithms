# -*- coding:utf-8 -*-
class Solution:
    # 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
    # def __init__(self):
    #     self.stack = []
    #     self.queue = []
    #     self.min_num = None

    # def push(self, node):
    #     # write code here
    #     if self.min_num is None:
    #         self.min_num = node
    #     elif node < self.min_num:
    #         self.min_num = node
    #     self.stack.append(node)
    #     self.queue = sorted(self.stack)

    # def pop(self):
    #     # write code here
    #     if not self.stack:
    #         return None
    #     top = self.stack.pop()
    #     self.queue.remove(top)
    #     self.min_num = self.queue[0]
    #     return top

    # def top(self):
    #     # write code here
    #     return self.stack[-1]

    # def min(self):
    #     # write code here
    #     return self.min_num

    # better

    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, node):
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]