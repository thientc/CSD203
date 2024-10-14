class Node:
    def __init__(self, value):
        self.value = value # Lưu trữ giá trị của nút
        self.next = None # Con trỏ trỏ đến nút tiếp theo, ban đầu là None
class SingleLinkedList:
    def __init__(self):
        self.head = None  # Head khởi tạo là None vì danh sách ban đầu rỗng

    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head  # Nút mới trỏ đến nút hiện tại ở đầu danh sách
        self.head = new_node        # Cập nhật head để trỏ đến nút mới
        return self.head
    def print(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    def addToTail(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:         # Duyệt đến nút cuối cùng
                current = current.next
            current.next = new_node # Gán nút cuối trỏ đến nút mới
    def addAfter(self, p, x):
        if p is None:
            print("The given previous node cannot be None.")
            return
        new_node = Node(x)   # Tạo một nút mới với giá trị x
        new_node.next = p.next  # Liên kết nút mới với nút tiếp theo của nút p
        p.next = new_node  # Gán nút tiếp theo của p là nút mới
    def traverse(self):
        current = self.head
        if current is None:
            print("the list is empty")
            return
        while current:
            print(f"Node value: {current.value}")
            current = current.next

    def deleteFromHead(self):
        if self.head is None:
            print("The list is empty. Cannot remove from head.")
            return None
        removed_node = self.head  # Nút bị xóa là nút head hiện tại
        self.head = self.head.next  # Cập nhật head thành nút tiếp theo
        print(f"Removed node with value: {removed_node.value}")
        return removed_node.value

    def deleteFromTail(self):
        if self.head is None:
            print("The list is empty. Cannot delete from tail.")
            return
        if self.head.next is None:  # Nếu danh sách chỉ có một nút
            print(f"Deleting node with value: {self.head.value}")
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        print(f"Deleting node with value: {current.next.value}")
        current.next = None  # Gán nút cuối cùng là None (loại bỏ nút cuối)
    def deleteAfter(self,p):
        if p is None or p.next is None:
            print("No node to delete")
            return None
        removed_node = p.next
        p.next = removed_node.next
        print(f'deleted node with value: {removed_node.value}')
        return removed_node.valuedêdefdedd
    def delete(self, x):
        current = self.head
        prev = None
        while current:
            if current.value == x:
                if prev is None:
                    print(f"Deleting head node with value: {current.value}")
                    self.head = current.next
                else:
                    print(f"Deleting node with value: {current.value}")
                    prev.next = current.next
                return
            prev = current
            current = current.next
        print(f"No node with value {x} found.")






