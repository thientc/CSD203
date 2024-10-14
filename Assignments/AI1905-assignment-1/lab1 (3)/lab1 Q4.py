class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. def addToHead(x) - thêm một nút với giá trị x vào đầu list
    def addToHead(self, x):
        new_node = Node(x)
        if not self.head:  # Nếu danh sách rỗng
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node
        print(f"Output của số 1: Đã thêm '{x}' vào đầu list.")

    # 2. def addToTail(x) - thêm một nút với giá trị x vào cuối list
    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:  # Nếu danh sách rỗng
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        print(f"Output của số 2: Đã thêm '{x}' vào đuôi list.")

    # 4. def traverse() - duyệt qua list và in giá trị của từng nút
    def traverse(self):
        if not self.head:
            print("Output của số 4: Danh sách rỗng.")
            return
        current = self.head
        print("Output của số 4: Duyệt list: ", end="")
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(đã quay lại đầu)")

    # 5. def deleteFromHead() - xóa nút ở đầu list và trả về giá trị của nó
    def deleteFromHead(self):
        if not self.head:
            return None
        deleted_value = self.head.value
        if self.head.next == self.head:  # Nếu chỉ có một nút
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        print(f"Output của số 5: Đã xóa phần tử ở đầu list: '{deleted_value}'.")
        return deleted_value

    # 6. def deleteFromTail() - xóa nút ở cuối list và trả về giá trị của nó
    def deleteFromTail(self):
        if not self.head:
            return None
        if self.head.next == self.head:  # Nếu chỉ có một nút
            deleted_value = self.head.value
            self.head = None
            print(f"Output của số 6: Đã xóa phần tử ở đuôi list: '{deleted_value}'.")
            return deleted_value
        current = self.head
        while current.next.next != self.head:
            current = current.next
        deleted_value = current.next.value
        current.next = self.head
        print(f"Output của số 6: Đã xóa phần tử ở đuôi list: '{deleted_value}'.")
        return deleted_value

    # 9. def search(x) - tìm kiếm và trả về nút đầu tiên có giá trị x
    def search(self, x):
        current = self.head
        if not current:
            print(f"Output của số 9: Không tìm thấy giá trị '{x}' trong list.")
            return None
        while True:
            if current.value == x:
                print(f"Output của số 9: Đã tìm thấy giá trị '{x}' trong list.")
                return current
            current = current.next
            if current == self.head:
                break
        print(f"Output của số 9: Không tìm thấy giá trị '{x}' trong list.")
        return None

    # 10. def count() - đếm và trả về số lượng nút trong list
    def count(self):
        if not self.head:
            print(f"Output của số 10: Số lượng phần tử trong list: 0.")
            return 0
        current = self.head
        count = 0
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        print(f"Output của số 10: Số lượng phần tử trong list: {count}.")
        return count

# Ví dụ sử dụng các hàm trên
cll = CircularLinkedList()

# Thêm các phần tử vào đầu và đuôi list
cll.addToHead(3)  # Số 1
cll.addToHead(2)  # Số 1
cll.addToTail(4)  # Số 2
cll.addToTail(5)  # Số 2

# Duyệt list và in các phần tử
cll.traverse()  # Số 4

# Xóa phần tử ở đầu list
deleted_head = cll.deleteFromHead()  # Số 5
cll.traverse()  # Số 4

# Xóa phần tử ở đuôi list
deleted_tail = cll.deleteFromTail()  # Số 6
cll.traverse()  # Số 4

# Tìm kiếm giá trị trong list
search_value = 4
search_result = cll.search(search_value)  # Số 9

# Đếm số lượng phần tử trong list
total_nodes = cll.count()  # Số 10
