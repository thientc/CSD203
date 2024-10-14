class Node:
    def __int__(self,data):
        self.data = data
        self.next = None

class singly_linked_list:
    def __init__(self):
        self.head = None

    def addToHead(self,x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def addToTail(self,x):
        new_node = Node(x)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def addAfter(self,p,x):
        new_node = Node(x)
        current = self.head
        while current and current.data != p:
            current = current.next
        if current:
            new_node.next = current.next
            current.next = new_node

    def traverse(self):

    def deleteFromHead(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def deleteFromTail(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def deleteAfter(self,p):
        current = self.head
        while current and current.data != p:
            current = current.next
        if current and current.next:
            data = current.next.data
            current.next = current.next.next
            return data
        return None

    def delValue(self,x):
        if self.head is None:
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != x:
            current = current.next
        if current.next:
            current.next = current.next.next

    def sort(self):

    def search(self,x):
        current = self.head
        while current:
            if current.data == x:
                print(f"Node with data {x} found at: {current}")
                return current
            current = current.next
        print(f"Node with data {x} not found.")
        return None

    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def delValue_P(self,p):

    def delValue_at_ith(self,i):

    def toArray(self):

    def addBefore(self,p,x):
        if self.head is None or self.head == p:
            self.addToHead(x)
            return
        current = self.head
        while current.next and current.next != p:
            current = current.next
        if current.next == p:
            new_node = Node(x)
            new_node.next = current.next
            current.next = new_node
    def max(self):
        if self.head is None:
            return None
        current = self.head
        max_val = current.data
        while current:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val
    def min(self):
        if self.head is None:
            return None
        current = self.head
        min_val = current.data
        while current:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val
    def sum(self):
        total = 0
        current = self.head
        while current:
            total += current.data
            current = current.next
        return total
    def avg(self):
        total = self.sum()
        count = self.count()
        return total / count if count > 0 else 0
    def sorted(self):

    def insert(self,x):

