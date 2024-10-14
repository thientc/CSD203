class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append((str(current.value)))
            current = current.next
        return '->'.join(values) + '->None'

    def addtohead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def addtotail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addafter(self, p, x):
        current = self.head
        while current and current.value != p:
            current = current.next
        if current:
            new_node = Node(x)
            new_node.next = current.next
            current.next = new_node

    def traverse(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.value)
            current = current.next
        while stack:
            print(stack.pop(), end=' -> ')
        print("None")

    def deletefromhead(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        return None

    def deletefromtail(self):
        if not self.head:
            return None
        if not self.head.next:
            value = self.head.value
            self.head = None
            return value
        current = self.head
        while current.next.next:
            current = current.next
        value = current.next.value
        current.next = None
        return value

    def deleteater(self, p):
        current = self.head
        while current and current.value != p:
            current = current.next
        if current and current.next:
            value = current.next.value
            current.next = current.next.next
            return value
        return None

    def delx(self, x):
        current = self.head
        temp = None
        while current and current.value != x:
            temp = current
            current = current.next
        if current:
            if temp:
                temp.next = current.next
            else:
                self.head = current.next

    def searchx(self, x):
        current = self.head
        while current:
            if current.value == x:
                return x
            current = current.next
        return None

    def count(self):
        total = 0
        current = self.head
        while current:
            total += 1
            current = current.next
        return total

    def del_i(self, i):
        pass

    def sort(self):
        pass

    def toarray(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.value)
            current = current.next
        return arr

    def addBefore(self, p, x):
        if not self.head:
            return
        if self.head.value == p:
            self.addtohead(x)
            return
        current = self.head
        while current.next and current.next.value != p:
            current = current.next
        if current.next:
            new_node = Node(x)
            new_node.next = current.next
            current.next = new_node

    def max1(self):
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head.next
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val

    def min1(self):
        if not self.head:
            return None
        min_val = self.head.value
        current = self.head.next
        while current:
            if current.value < min_val:
                min_val = current.value
            current = current.next
        return min_val

    def sum1(self):
        current = self.head
        total = 0
        while current:
            total += current.value
            current = current.next
        return total

    def avg1(self):
        total = self.sum1()
        count = self.count()
        if count == 0:
            return None
        return total / count


check = LinkedList()
check.addtohead(6)
check.addtohead(5)
check.addtohead(4)
check.addtohead(3)
check.addtohead(1)
print(check.addBefore(5, 10))
