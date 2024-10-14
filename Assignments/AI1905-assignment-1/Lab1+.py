class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        if not self.head:
            return "Danh sách trống"  # Trả về chuỗi nếu danh sách trống

        nodes = []
        current = self.head
        while current:
            nodes.append(f"[{current.data}]")
            current = current.next

        return "Head -> " + " -> ".join(nodes) + " -> Tail"
    def addtoHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def addtoTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
                current.next = new_node

    def addAfter(self,p,x):
        if p is None:
            return
        new_node = Node(x)
        new_node.next = p.next
        p.next = new_node


    def deleteFromHead(self):
        if not self.head:
            return
        data = self.head.next
        self.head = self.head.next
        return data

    def deleteFromTail(self):
        if not self.head:
            return None
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data
        current = self.head
        while current.next.next:
            current = current.next
        data = current.next.data
        current.next = None
        return data

    def deleteAter(self,p):
        if p is None or p.next is None:
            return None
        data = p.next.data
        p.next = p.next.next
        return data

    def delete(self,x):
        current = self.head
        if not current:
            return
        if current.data == x:
            self.head = current.next
            return
        while current.next and current.next.next != x:
            current = current.next
        if current.next:
            current.next= current.next.next

    def search(self,x):
        current = self.head
        while current:
            if current.data == x:
                return current
            current = current.next
        return None

    def count(self):
        current = self.head
        count = 0
        while current:
            count =+ 1
            current = current.next
        return count

    def sort(self):
        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True
    def toArray(self):
        ar = []
        current = self.head
        while current:
            ar.append(current.data)
            current = current.next
        return ar

    def max(self):
        if not self.head:
            return
        max = self.head.data
        current = self.head
        while current:
            if current.data > max:
                max = current.data
            current = current.next
        return max

    def min(self):
        if not self.head:
            return
        min = self.head.data
        current = self.head
        while current:
            if current.data < min:
                min = current
            current = current.next
        return min









