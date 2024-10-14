class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_in_ascending_order(self, new_node):
        if self.head is None:
            self.append(new_node)
            return
    
        if new_node.data < self.head.data:
            self.prepend(new_node)
            return
        
        current = self.head
        while True:
            if current.next is None:
                self.append(new_node)
                break
            if new_node.data < current.next.data:
                insert_point_next = current.next
                new_node.next = insert_point_next
                current.next = new_node
                break
            current = current.next
    
    def __repr__(self):
        _repr = '['
        current = self.head
        while current is not None:
            _repr = f'{_repr}{repr(current.data)}, '
            current = current.next
        if _repr.endswith(', '):
            _repr = _repr[:-2]
        return f'{_repr}]'

lst = LinkedList()
for i in [8, 3, 6, 2, 5, 9, 4, 1, 7]:
    lst.insert_in_ascending_order(Node(i))
print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9]