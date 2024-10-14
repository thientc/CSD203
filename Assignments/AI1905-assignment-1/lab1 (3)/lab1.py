class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. def addToHead(x)
    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node
        print(f"Output của số 1: Đã thêm '{x}' vào đầu list.")

    # 2. def addToTail(x)
    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Output của số 2: Đã thêm '{x}' vào đuôi list.")

    # 4. def traverse()
    def traverse(self):
        current = self.head
        print("Output của số 4: Duyệt list: ", end="")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    # 5. def deleteFromHead()
    def deleteFromHead(self):
        if not self.head:
            return None
        deleted_value = self.head.value
        self.head = self.head.next
        print(f"Output của số 5: Đã xóa phần tử ở đầu list: '{deleted_value}'.")
        return deleted_value

    # 6. def deleteFromTail()
    def deleteFromTail(self):
        if not self.head:
            return None
        if not self.head.next:
            deleted_value = self.head.value
            self.head = None
            print(f"Output của số 6: Đã xóa phần tử ở đuôi list: '{deleted_value}'.")
            return deleted_value
        current = self.head
        while current.next.next:
            current = current.next
        deleted_value = current.next.value
        current.next = None
        print(f"Output của số 6: Đã xóa phần tử ở đuôi list: '{deleted_value}'.")
        return deleted_value

    # 9. def search(x)
    def search(self, x):
        current = self.head
        while current:
            if current.value == x:
                print(f"Output của số 9: Đã tìm thấy giá trị '{x}' trong list.")
                return current
            current = current.next
        print(f"Output của số 9: Không tìm thấy giá trị '{x}' trong list.")
        return None

    # 10. def count()
    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        print(f"Output của số 10: Số lượng phần tử trong list: {count}.")
        return count

# Ví dụ sử dụng các hàm trên
sll = SinglyLinkedList()

# Thêm các phần tử vào đầu và đuôi list
sll.addToHead(3)
sll.addToHead(2)
sll.addToTail(4)
sll.addToTail(5)

# Duyệt list và in các phần tử
sll.traverse()

# Xóa phần tử ở đầu list
deleted_head = sll.deleteFromHead()
sll.traverse()

# Xóa phần tử ở đuôi list
deleted_tail = sll.deleteFromTail()
sll.traverse()

# Tìm kiếm giá trị trong list
search_value = 4
search_result = sll.search(search_value)

# Đếm số lượng phần tử trong list
total_nodes = sll.count()
