class node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.tail = node(None)

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
            if cur is None:
                return -1
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        cur = node(val, self.head.next)
        self.head.next = cur
        if self.tail.val is None:
            self.tail = cur

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.tail.next = node(val)
        self.tail = self.tail.next
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        cur = self.head
        for _ in range(index):
            cur = cur.next
            if cur is None:
                return
        new = node(val, cur.next)
        cur.next = new
        if self.tail == cur:
            self.tail = new
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        cur = self.head
        for _ in range(index):
            cur = cur.next
            if cur is None:
                return
        if self.tail == cur.next:
            self.tail = cur
        if cur.next:
            cur.next = cur.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)