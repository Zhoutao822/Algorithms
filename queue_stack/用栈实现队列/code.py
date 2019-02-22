class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.tmp = []
        self.h = None

    def push(self, x: 'int') -> 'None':
        """
        Push element x to the back of queue.
        """
        if not self.queue:
            self.h = x
        self.queue.append(x)

    def pop(self) -> 'int':
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.queue) == 1:
            return self.queue.pop()
        for _ in range(len(self.queue) - 1):
            self.tmp.append(self.queue.pop())
        self.h = self.tmp[-1] 
        p = self.queue.pop()
        for _ in range(len(self.tmp)):
            self.queue.append(self.tmp.pop())
        return p

    def peek(self) -> 'int':
        """
        Get the front element.
        """
        return self.h

    def empty(self) -> 'bool':
        """
        Returns whether the queue is empty.
        """
        return True if len(self.queue) == 0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()