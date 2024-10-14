class Node:
    def __init__(self, value):
        self.value = value
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

    def addBefore(self, p, x):
        if not self.head or p == self.head:
            self.addToHead(x)
            return
        temp = self.head
        while temp and temp.next != p:
            temp = temp.next
        if temp:
            new_node = Node(x)
            new_node.next = temp.next
            temp.next = new_node

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next
        print()

    def deleteFromHead(self):
        if not self.head:
            return None
        info = self.head.value
        self.head = self.head.next
        return info

    def deleteFromTail(self):
        if not self.head:
            return None
        if not self.head.next:
            info = self.head.value
            self.head = None
            return info
        temp = self.head
        while temp.next.next:
            temp = temp.next
        info = temp.next.value
        temp.next = None
        return info

    def deleteAfter(self, p):
        if not p or not p.next:
            return None
        info = p.next.value
        p.next = p.next.next
        return info

    def delete(self, x):
        if not self.head:
            return None
        if self.head.value == x:
            return self.deleteFromHead()
        temp = self.head
        while temp.next and temp.next.value != x:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def search(self, x):
        temp = self.head
        while temp:
            if temp.value == x:
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
        if i == 0:
            return self.deleteFromHead()
        temp = self.head
        for _ in range(i - 1):
            if not temp.next:
                return None
            temp = temp.next
        if temp.next:
            info = temp.next.value
            temp.next = temp.next.next
            return info
        return None

    def sort(self):
        if not self.head or not self.head.next:
            return
        temp = self.head
        arr = []
        while temp:
            arr.append(temp.value)
            temp = temp.next
        arr.sort()
        temp = self.head
        for val in arr:
            temp.value = val
            temp = temp.next

    def toArray(self):
        arr = []
        temp = self.head
        while temp:
            arr.append(temp.value)
            temp = temp.next
        return arr

    def merge(self, other):
        merged_list = SinglyLinkedList()
        p1 = self.head
        p2 = other.head
        while p1 and p2:
            if p1.value < p2.value:
                merged_list.addToTail(p1.value)
                p1 = p1.next
            else:
                merged_list.addToTail(p2.value)
                p2 = p2.next
        while p1:
            merged_list.addToTail(p1.value)
            p1 = p1.next
        while p2:
            merged_list.addToTail(p2.value)
            p2 = p2.next
        return merged_list

    def attach(self, other):
        if not self.head:
            self.head = other.head
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = other.head

    def max(self):
        if not self.head:
            return None
        max_val = self.head.value
        temp = self.head
        while temp:
            if temp.value > max_val:
                max_val = temp.value
            temp = temp.next
        return max_val

    def min(self):
        if not self.head:
            return None
        min_val = self.head.value
        temp = self.head
        while temp:
            if temp.value < min_val:
                min_val = temp.value
            temp = temp.next
        return min_val

    def sum(self):
        total = 0
        temp = self.head
        while temp:
            total += temp.value
            temp = temp.next
        return total

    def avg(self):
        total = self.sum()
        count = self.count()
        return total / count if count != 0 else 0

    def isSorted(self):
        if not self.head or not self.head.next:
            return True
        temp = self.head
        while temp.next:
            if temp.value > temp.next.value:
                return False
            temp = temp.next
        return True

    def insert(self, x):
        new_node = Node(x)
        if not self.head or self.head.value >= x:
            self.addToHead(x)
            return
        temp = self.head
        while temp.next and temp.next.value < x:
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

    def isEqual(self, other):
        temp1 = self.head
        temp2 = other.head
        while temp1 and temp2:
            if temp1.value != temp2.value:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return temp1 is None and temp2 is None

ll1 = SinglyLinkedList()
ll1.addToHead(100)
ll1.addToTail(100023)
ll1.addToTail(439532587)
ll1.traverse()
print("Max:", ll1.max())
print("Min:", ll1.min())
ll1.reverse()
ll1.traverse()
#Question 2
ll1.addToHead("apple")
ll1.addToTail("banana")
ll1.addToTail("cherry")
ll1.traverse()
banana_node = ll1.search("banana")
ll1.addAfter(banana_node, "date")
ll1.traverse()
print("Deleted from head:", ll1.deleteFromHead())
ll1.traverse()
print("Deleted from tail:", ll1.deleteFromTail())
ll1.traverse()
ll1.delete("banana")
ll1.traverse()
print("Count of nodes:", ll1.count())