class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # Thêm con trỏ prev cho danh sách liên kết đôi

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 1. def addToHead(x)
    def addToHead(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print(f"Output của số 1: Đã thêm '{x}' vào đầu list.")

    # 2. def addToTail(x)
    def addToTail(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        print(f"Output của số 2: Đã thêm '{x}' vào đuôi list.")

    # 4. def traverse()
    def traverse(self):
        current = self.head
        print("Output của số 4: Duyệt list: ", end="")
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    # 5. def deleteFromHead()
    def deleteFromHead(self):
        if not self.head:
            return None
        deleted_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        print(f"Output của số 5: Đã xóa phần tử ở đầu list: '{deleted_value}'.")
        return deleted_value

    # 6. def deleteFromTail()
    def deleteFromTail(self):
        if not self.tail:
            return None
        deleted_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
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
dll = DoublyLinkedList()

# Thêm các phần tử vào đầu và đuôi list
dll.addToHead(3)  # Số 1
dll.addToHead(2)  # Số 1
dll.addToTail(4)  # Số 2
dll.addToTail(5)  # Số 2

# Duyệt list và in các phần tử
dll.traverse()  # Số 4

# Xóa phần tử ở đầu list
deleted_head = dll.deleteFromHead()  # Số 5
dll.traverse()  # Số 4

# Xóa phần tử ở đuôi list
deleted_tail = dll.deleteFromTail()  # Số 6
dll.traverse()  # Số 4

# Tìm kiếm giá trị trong list
search_value = 4
search_result = dll.search(search_value)  # Số 9

# Đếm số lượng phần tử trong list
total_nodes = dll.count()  # Số 10
