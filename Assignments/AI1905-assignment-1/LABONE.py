class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            #check if the list is emty
            self.head = neww_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def addAfter(self, p, x):
        new_node = Node(x)
        current = self.head
        while current and current.value != p:
            current = current.next
        if current:
            new_node.next = current.next
            current.next = new_node
        else: print(f"Value of {p} is not found")

    def delete(self, x):
        del_node = Node(x)
        current = self.head
        while current and current.value != x:
            current = current.next
        if current:
            current = current.next
            current.next = None
        else: print(f"Value of {x} is not exist")


    def deleteFromHead(self):
        current = self.head
        while current:
            current = current.next
            print(current)

    def display(self):
        current = self.head
        while current:
            print(current.value, end = " --> ")
            current = current.next


if __name__ == "__main__":
    integers = SinglyLinkList()
    integers.addToHead(13)
    integers.addToHead(22)
    integers.addToTail(11)
    print(integers.display())
    integers.addAfter(13, 9)
    integers.delete(9)
    print(integers.display())
