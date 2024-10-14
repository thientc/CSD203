import sys
sys.tracebacklimit = 0

class SingleList:
    __slots__ = "_head", "_size", "_tail"
    class _Node:
        __slots__ = "integer", "next"

        def __init__(self, number:int, next) -> None:
            self.integer = number
            self.next = next

    def __init__(self) -> None:
        self._head = None
        self._tail = self._head
        self._size = 0

    def addToHead(self, x:int):
        self._head = self._Node(x, self._head)
        if self._size == 0:
            self._tail = self._head
        self._size +=1
        # self._head = new_node
    def addAfter(self, p: int, x: int):
        if self._size == 0:
            raise Exception("List is empty")
        head = self._head
        while head and head.integer != p:
            head = head.next
        if not head:
            raise Exception("Value {0} not found in list!".format(p))
        head.next = self._Node(x, head.next)
        self._size += 1

l = SingleList()
l.addToHead(1)
l.addToHead(2)
l.addToHead(3)
l.addAfter(6,5)
el = l._head

while el:
    print(el.integer)
    el = el.next