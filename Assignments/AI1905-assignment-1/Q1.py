class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def addAfter(self, p, x):
        if not p:
            return
        new_node = Node(x)
        new_node.next = p.next
        p.next = new_node

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def deleteFromHead(self):
        if self.head:
            deleted_info = self.head.data
            self.head = self.head.next
            return deleted_info
        return None

    def deleteFromTail(self):
        if not self.head:
            return None
        if not self.head.next:
            deleted_info = self.head.data
            self.head = None
            return deleted_info
        temp = self.head
        while temp.next.next:
            temp = temp.next
        deleted_info = temp.next.data
        temp.next = None
        return deleted_info

    def deleteAfter(self, p):
        if p and p.next:
            deleted_info = p.next.data
            p.next = p.next.next
            return deleted_info
        return None

    def delete(self, x):
        temp = self.head
        if temp and temp.data == x:
            self.head = temp.next
            return
        while temp and temp.next:
            if temp.next.data == x:
                temp.next = temp.next.next
                return
            temp = temp.next

    def search(self, x):
        temp = self.head
        while temp:
            if temp.data == x:
                return temp
            temp = temp.next
        return None

    def count(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def deleteAt(self, i):
        if i < 0:
            return None
        temp = self.head
        if i == 0:
            return self.deleteFromHead()
        for _ in range(i-1):
            if not temp.next:
                return None
            temp = temp.next
        if temp.next:
            return self.deleteAfter(temp)
        return None

    def sort(self):
        if not self.head or not self.head.next:
            return
        sorted_list = None
        while self.head:
            min_node = self.head
            temp = self.head.next
            while temp:
                if temp.data < min_node.data:
                    min_node = temp
                temp = temp.next
            self.delete(min_node.data)
            if not sorted_list:
                sorted_list = Node(min_node.data)
                sorted_tail = sorted_list
            else:
                sorted_tail.next = Node(min_node.data)
                sorted_tail = sorted_tail.next
        self.head = sorted_list

    def deleteNode(self, p):
        if not self.head or not p:
            return
        if self.head == p:
            self.head = self.head.next
            return
        temp = self.head
        while temp and temp.next != p:
            temp = temp.next
        if temp:
            temp.next = p.next

    def toArray(self):
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.data)
            temp = temp.next
        return arr

    def addBefore(self, p, x):
        if not p or not self.head:
            return
        if self.head == p:
            self.addToHead(x)
            return
        temp = self.head
        while temp and temp.next != p:
            temp = temp.next
        if temp:
            new_node = Node(x)
            new_node.next = p
            temp.next = new_node

    def merge(self, other):
        merged_list = SinglyLinkedList()
        p1, p2 = self.head, other.head
        while p1 and p2:
            if p1.data <= p2.data:
                merged_list.addToTail(p1.data)
                p1 = p1.next
            else:
                merged_list.addToTail(p2.data)
                p2 = p2.next
        while p1:
            merged_list.addToTail(p1.data)
            p1 = p1.next
        while p2:
            merged_list.addToTail(p2.data)
            p2 = p2.next
        return merged_list

    def attach(self, other):
        if not self.head:
            self.head = other.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = other.head

    def max(self):
        if not self.head:
            return None
        max_val = self.head.data
        temp = self.head.next
        while temp:
            if temp.data > max_val:
                max_val = temp.data
            temp = temp.next
        return max_val

    def min(self):
        if not self.head:
            return None
        min_val = self.head.data
        temp = self.head.next
        while temp:
            if temp.data < min_val:
                min_val = temp.data
            temp = temp.next
        return min_val

    def sum(self):
        total = 0
        temp = self.head
        while temp:
            total += temp.data
            temp = temp.next
        return total

    def avg(self):
        total = self.sum()
        count = self.count()
        if count == 0:
            return None
        return total / count

    def isSorted(self):
        if not self.head or not self.head.next:
            return True
        temp = self.head
        while temp.next:
            if temp.data > temp.next.data:
                return False
            temp = temp.next
        return True

    def insert(self, x):
        new_node = Node(x)
        if not self.head or self.head.data >= x:
            self.addToHead(x)
            return
        temp = self.head
        while temp.next and temp.next.data < x:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def equals(self, other):
        p1, p2 = self.head, other.head
        while p1 and p2:
            if p1.data != p2.data:
                return False
            p1, p2 = p1.next, p2.next
        return p1 is None and p2 is None

