class Node:
    __slots__ = '_value', '_next'
    def __init__(self,value):
        self._value = value
        self._next = None

class Singly_Linked_List:
    def __init__(self):
        self._head = None

    def addToHead(self,x):
        new_Node = Node(x)
        new_Node._next = self._head
        self._head = new_Node

    def addToTail(self,x):
        new_Node = Node(x)
        if not self._head:
            self._head = new_Node
        else:
            tail = self._head
            while tail._next:
                tail = tail._next
            tail._next = new_Node

    def addAfter(self,p,x):
        if p is None:
            print("The p node isn't exist, can't add after it ")
            return
        new_Node = Node(x)
        new_Node._next = p._next
        p._next = new_Node

    def traverse(self):
        current = self._head
        while current:
            print(current._value, end=' ')
            current = current._next
        print("/End")

    def deleteFromHead(self):
        if not self._head:
            return None
        value = self._head._value
        self._head = self._head._next
        return value

    def deleteFromTail(self):
        if not self._head:
            return None
        if not self._head._next:
            value = self._head
            self._head = None
            return value
        current = self._head
        while current._next._next:
            current = current._next
        value = current._next._value
        current._next = None
        return value

    def Del(self,x):
        if not self._head:
            return None
        if self._head._value == x:
            self._head = self._head._next
            return
        current = self._head
        while (current._next and current._next._value) != x:
            current = current._next
        if current._next != None:
            current._next = current._next._next

if __name__ == '__main__':
    linked_list = Singly_Linked_List()
    linked_list.addToHead(5)
    linked_list.addToHead(2)
    linked_list.addToTail(3)
    linked_list.Del(5)
    linked_list.traverse()












