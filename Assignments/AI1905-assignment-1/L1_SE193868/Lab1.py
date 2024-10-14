class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self,x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def addToTail(self,x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node

    def addAfter(self,p,x):
        if p is None:
            print("Given previous node must i=be in a linked list")
            return
        new_node = Node(x)
        new_node.next = p.next
        p.next = new_node

    def traverse(self):
        if not self.head:
            print("The list is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def deleteFromHead(self):
        if self.head is None:
            print("The list is empty")
            return
        self.head = self.head.next

    def deleteFromTail(self):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.next is None:
            self.head = None
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def deleteAfter(self,p):
        if p is None or p.next is None:
            print("The given node is either None or does not have a next node")
            return
        node_delete = p.next
        p.next = node_delete.next
        node_delete.next = None

    def deleteFromHeadByValue(self,x):
        if self.head is None:
            print("The list is empty")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != x:
            current = current.next
        if current.next is None:
            print(f"The node with the value {x} not found")
            return
        current.next = current.next.next

    def delete_i(self,i):
        if self.head is None:
            print("The list is empty")
            return
        if i == 0:
            self.head = self.head.next
            return
        current = self.head
        for j in range(i-1):
            if current is None or current.next is None:
                print(f"Index {i} is oyt of bound")
                return
            current = current.next
        if current.next is None:
            print(f"Index {i} is out of bound")
            return
        current.next = current.next.next

    def delete_p(self,p):
        if self.head is None:
            print("The list is empty")
            return
        if self.head == p:
            self.head = self.head.next
            p.next = None
            return
        prev = None
        current = self.head
        while current and current != p:
            prev = current
            current = current.next
        if current == p:
            prev.next = current.next
            current.next = None
        else:
            print("Node not found")

    def sort(self):
        if not self.head or not self.head.next:
            return
        sorting = True
        while sorting:
            sorting = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    current.data,current.next.data = current.next.data,current.data
                    sorting = True
                current = current.next

    def sorted(self):
        if not self.head or not self.head.next:
            return True
        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    def search(self,x):
        current = self.head
        while current:
            if current.data == x:
                print(f"The searching node is: {current.data}")
                return True
            current = current.next
        return False

    def count(self):
        if self.head is None:
            print("The list is empty")
            return
        counting = 0
        current = self.head
        while current:
            counting += 1
            current = current.next
        print(f"There are {counting} node in the list")
        return

    def findMax(self):
        if not self.head:
            return None
        max_value = self.head.data
        current = self.head.next
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next
        return max_value

    def findMin(self):
        if not self.head:
            return None
        min_value = self.head.data
        current = self.head.next
        while current:
            if current.data > min_value:
                min_value = current.data
            current = current.next
        return min_value

    def findSum(self):
        if not self.head:
            return None
        total = 0
        current = self.head
        while current:
            total += current.data
            current = current.next
        return total

    def findAvg(self):
        if not self.head:
            return None
        total = 0
        count = 0
        current = self.head
        while current:
            total += current.data
            count += 1
            current = current.next
        return total / count if count > 0 else None

    def toArray(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr















