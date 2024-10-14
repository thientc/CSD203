class Empty(Exception):
    pass
class SingleLinkedList:
    class Node:
        def __init__(self, data):
            self._data = data
            self._next = None
        def get_data(self):
            return self._data
        def get_next(self):
            return self._next
        def set_next(self, next_node):
            self._next = next_node
    def __init__(self):
        self._size = 0
        self._head = None
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size == 0
    def addToHead(self, data):
        new_val = self.Node(data)
        if not self.is_empty():
            new_val.set_next(self._head)
        self._head = new_val
        self._size += 1
    def addToTail(self, data):
        new_val = self.Node(data)
        if self.is_empty():
            self._head = new_val
        else:
            current = self._head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_val)
        self._size += 1
    def addAfter(self, p, data):
        head_val = self._head
        new_val =self.Node(data)
        while head_val.get_next() != None:
            if head_val.get_data() == p:
                new_val.set_next(head_val.get_next())
                head_val.set_next(new_val)
                self._size += 1
            head_val = head_val.get_next()
    def display(self):
        current = self._head
        while current != None:
            print(current.get_data(), end=" ")
            current = current.get_next()
    def deleteFromHead(self):
        if self.is_empty():
            raise Empty("List is empty, cannot delete.")
        self._head = self._head.get_next()
        self._size -= 1

    def deleteFromTail(self):
        if self.is_empty():
            raise Empty("List is empty, cannot delete.")
        else:
            head_val = self._head
            ke_cuoi = None
            while head_val.get_next() != None:
                ke_cuoi = head_val  #Chạy song song ke cuoi se la con tro truoc head_val(con tro cuoi)
                head_val = head_val.get_next()
            ke_cuoi.set_next(None) #Xoa head_val va cap nhat con tro ke_cuoi chi vao none
        self._size -= 1
if __name__ == "__main__":
    linked_list = SingleLinkedList()
    linked_list.addToHead(3)
    linked_list.addToHead(2)
    linked_list.addToHead(1)
    linked_list.addToTail(4)
    linked_list.addToTail(5)
    linked_list.addToHead(10)
    linked_list.addAfter(2,9)
    linked_list.deleteFromHead()
    linked_list.deleteFromTail()
    linked_list.display()
