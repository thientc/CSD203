class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    # 1. Add a node with value x at the head of the list
    def addToHead(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
    # 2. Add a node with value x at the tail of the list
    def addToTail(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            self.size += 1
    # 3. Add a node with value x after the node p
    def addAfter(self, p, x):
        current = self.head
        while current is not None and current != p:
            current = current.next
        if current is None:
            print("Node p not found in the list.")
            self.size += 1
        else:
            new_node = Node(x)
            new_node.next = current.next
            current.next = new_node
            self.size += 1
    # 4. Traverse from head to tail and display the info of all nodes in the list
    def traverse(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    # 5. Delete the head node and return its value
    def deleteFromHead(self):
        if self.head is None:
            return
        curr = self.head
        self.head = curr.next
        self.size -= 1
    # 6. Delete the tail node and return its value
    def deleteFromTail(self):
        if self.head is None:
            return
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
            self.size -= 1
    # 7. Delete the node after node p and return its value
    def deleteAfter(self, p):
        current = self.head
        while current and current != p:
            current = current.next
        if current is None or current.next is None:
            print("No node to delete after the given node.")
            return None
        else:
            value = current.next.value
            current.next = current.next.next
            return value
    # 8. Delete the first node with value x
    def delete(self, x):
        if x < 0 or x > self.size:
            return
        elif x == 1:
            self.deleteFromHead()
        else:
            curr = self.head
            for i in range(1, x - 1):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1
# Example usage:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.addToHead(2)
    linked_list.addToTail(4)
    linked_list.addToTail(6)
    linked_list.addToTail(9)
    print("Danh sách gốc:")
    p = linked_list.head.next
    linked_list.addAfter(p, 5)
    linked_list.traverse()
    print("Xóa cái đầu", linked_list.deleteFromHead())
    linked_list.traverse()
    print("Xóa cái đuôi:", linked_list.deleteFromTail())
    linked_list.traverse()
    print("Xóa giá trị:", linked_list.deleteAfter(p))
    linked_list.traverse()
    print("Xóa vị trí:", linked_list.delete(2))
    linked_list.traverse()