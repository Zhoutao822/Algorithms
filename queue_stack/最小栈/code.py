class MinStack:

    def __init__(self):
        """
        url: https://leetcode-cn.com/explore/learn/card/queue-stack/218/stack-last-in-first-out-data-structure/877/
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: 'int') -> 'None':
        self.stack.append(x)
        self.min = min(self.stack)

    def pop(self) -> 'None':
        if not self.stack:
            return
        self.stack.pop()
        if self.stack:
            self.min = min(self.stack)

    def top(self) -> 'int':
        return self.stack[-1]

    def getMin(self) -> 'int':
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()