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
        print(f"Thêm '{x}' vào đầu list.")

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
        print(f"Thêm '{x}' vào đuôi list.")

    # 3. def addAfter(p, x)
    def addAfter(self, p, x):
        new_node = Node(x)
        current = self.head
        while current:
            if current == p:
                new_node.next = current.next
                current.next = new_node
                print(f"Thêm '{x}' sau '{p.value}'.")
                return
            current = current.next

    # 4. def traverse()
    def traverse(self):
        current = self.head
        print("Duyệt list: ", end="")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    # 5. def deleteFromHead()
    def deleteFromHead(self):
        if not self.head:
            print("list rỗng, không thể xóa đầu.")
            return None
        deleted_value = self.head.value
        self.head = self.head.next
        print(f"Đã xóa phần tử ở đầu list: '{deleted_value}'.")
        return deleted_value

    # 6. def deleteFromTail()
    def deleteFromTail(self):
        if not self.head:
            print("list rỗng, không thể xóa đuôi.")
            return None
        if not self.head.next:
            deleted_value = self.head.value
            self.head = None
            print(f"Đã xóa phần tử ở đuôi list: '{deleted_value}'.")
            return deleted_value
        current = self.head
        while current.next.next:
            current = current.next
        deleted_value = current.next.value
        current.next = None
        print(f"Đã xóa phần tử ở đuôi list: '{deleted_value}'.")
        return deleted_value

    # 7. def deleteAfter(p)
    def deleteAfter(self, p):
        if not p or not p.next:
            print("Không thể xóa phần tử sau nút đã cho.")
            return None
        deleted_value = p.next.value
        p.next = p.next.next
        print(f"Đã xóa phần tử sau '{p.value}': '{deleted_value}'.")
        return deleted_value

    # 8. def del(x)
    def delete(self, x):
        if not self.head:
            print("list rỗng, không thể xóa.")
            return None
        if self.head.value == x:
            self.head = self.head.next
            print(f"Đã xóa phần tử '{x}' khỏi list.")
            return
        current = self.head
        while current.next:
            if current.next.value == x:
                current.next = current.next.next
                print(f"Đã xóa phần tử '{x}' khỏi list.")
                return
            current = current.next
        print(f"Không tìm thấy phần tử '{x}' để xóa.")

    # 9. def search(x)
    def search(self, x):
        current = self.head
        while current:
            if current.value == x:
                print(f"Đã tìm thấy '{x}' trong list.")
                return current
            current = current.next
        print(f"Không tìm thấy '{x}' trong list.")
        return None

    # 10. def count()
    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        print(f"Số lượng phần tử trong list: {count}.")
        return count

# Ví dụ sử dụng các hàm trên
sll = SinglyLinkedList()

# 1. Thêm các phần tử vào đầu và đuôi list
sll.addToHead("apple")  # Số 1
sll.addToHead("banana")  # Số 1
sll.addToTail("cherry")  # Số 2
sll.addToTail("date")  # Số 2

# 4. Duyệt list và in các phần tử
sll.traverse()

# 3. Thêm phần tử sau một phần tử cụ thể
p = sll.search("banana")
if p:
    sll.addAfter(p, "blueberry")
sll.traverse()

# 5. Xóa phần tử ở đầu list
sll.deleteFromHead()
sll.traverse()

# 6. Xóa phần tử ở đuôi list
sll.deleteFromTail()
sll.traverse()

# 7. Xóa phần tử sau một nút cụ thể
if p:
    sll.deleteAfter(p)
    sll.traverse()

# 8. Xóa nút có giá trị bằng "cherry"
sll.delete("cherry")
sll.traverse()

# 9. Tìm kiếm giá trị trong list
search_value = "blueberry"
sll.search(search_value)

# 10. Đếm số lượng phần tử trong
sll.count()
