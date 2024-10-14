class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def print_list(self):
        current = self._head
        if current is None:
            print("Danh sách rỗng.")
            return
        while current:
            print(current._data, end=' -> ')
            current = current._next
        print('None')

    def addToHead(self, x):
        newest = Node(x)
        newest._next =self._head
        self._head = newest

    def addToTail(self, x):
        newest = Node(x)
        if not self._head:
            self._head = newest
            return
        last = self._head
        while last._next:
            last = last._next
        last._next = newest

    def addAfter(self, p, x):
        if p is None:
            print("Node p does not exist.")
            return
        newest = Node(x)
        newest._next = p._next
        p._next = newest

    def traverse(self):
        current = self._head
        while current:
            print(current._data, end=' -> ')
            current = current._next
        print('None')

    def deleteFromHead(self):
        if self._head is None :
            return None
        remove = self._head._data
        self._head = self._head._next
        return remove

    def deleteFromTail(self):
        if self._head is None:
            return None
        if self._head._next is None:
            removed_data = self._head._data
            self._head = None
            return removed_data
        current = self._head
        while current._next and current._next._next:
            current = current._next
        removed_data = current._next._data
        current._next = None
        return removed_data

    def deleteAfter(self, p):
        if p is None or p._next is None:
            return None
        removed_data = p._next._data
        p._next = p._next._next
        return removed_data

    def delByValue(self, x):
        current = self._head
        if current and current._data == x:
            self._head = current._next
            return

        prev = None
        while current and current._data != x:
            prev = current
            current = current._next

        if current:
            prev._next = current._next

    def search(self, x):
        current = self._head
        while current:
            if current._data == x:
                return current
            current = current._next
        return None

    def count(self):
        current = self._head
        count = 0
        while current:
            count += 1
            current = current._next
        return count

    def deleteAtIndex(self, i):
        if i < 0 or i >= self.count():
            return None
        current = self._head
        if i == 0:
            return self.deleteFromHead()

        prev = None
        for _ in range(i):
            prev = current
            current = current._next
        removed_data = current._data
        prev._next = current._next
        return removed_data

    def sort(self):
        if self._head is None or self._head._next is None:
            return
        sorted_list = None
        current = self._head
        while current:
            next_node = current._next
            sorted_list = self.sortedInsert(sorted_list, current)
            current = next_node
        self._head = sorted_list

    def sortedInsert(self, head, new_node):
        if head is None or head._data >= new_node._data:
            new_node._next = head
            return new_node
        current = head
        while current._next and current._next._data < new_node._data:
            current = current._next
        new_node._next = current._next
        current._next = new_node
        return head

    def delNode(self, p):
        if self._head is None or p is None:
            return
        if self._head == p:
            self._head = self._head._next
            return
        current = self._head
        while current._next:
            if current._next == p:
                current._next = current._next._next
                return
            current = current._next

    def toArray(self):
        array = []
        current = self._head
        while current:
            array.append(current._data)
            current = current._next
        return array

    def merge(self, other):
        if not self._head:
            return other
        if not other._head:
            return self

        merged_head = None
        if self._head._data <= other._head._data:
            merged_head = self._head
            self._head = self._head._next
        else:
            merged_head = other._head
            other._head = other._head._next

        current = merged_head
        while self._head and other._head:
            if self._head._data <= other._head._data:
                current._next = self._head
                self._head = self.head._next
            else:
                current._next = other._head
                other._ = other._head._next
            current = current._next

        current._next = self._head if self._head else other._head
        return merged_head

    def addBefore(self, p, x):
        if p is None or self.head is None:
            print("Node p does not exist or list is empty.")
            return
        new_node = Node(x)
        if self._head == p:
            new_node.next = self._head
            self._head = new_node
            return
        current = self.head
        while current._next and current._next != p:
            current = current._next
        if current._next == p:
            new_node._next = p
            current._next = new_node

    def attach(self, other):
        if not self._head:
            self._head = other._head
            return
        last = self._head
        while last._next:
            last = last._next
        last._next = other._head

    def max(self):
        if self._head is None:
            return None
        max_value = self._head._data
        current = self._head
        while current:
            if current._data > max_value:
                max_value = current._data
            current = current._next
        return max_value

    def min(self):
        if self._head is None:
            return None
        min_value = self._head._data
        current = self._head
        while current:
            if current._data < min_value:
                min_value = current._data
            current = current._next
        return min_value

    def sum(self):
        total = 0
        current = self._head
        while current:
            total += current._data
            current = current._next
        return total

    def avg(self):
        count = self.count()
        return self.sum() / count if count > 0 else 0

    def is_sorted(self):
        current = self._head
        while current and current._next:
            if current._data > current._next._data:
                return False
            current = current._next
        return True

    def insert(self, x):
        new_node = Node(x)
        if self._head is None or self._head._data >= new_node._data:
            new_node._next = self._head
            self._head = new_node
            return
        current = self._head
        while current._next and current._next._data < new_node._data:
            current = current._next
        new_node._next = current._next
        current.next = new_node

    def reverse(self):
        prev = None
        current = self._head
        while current:
            next_node = current._next
            current._next = prev
            prev = current
            current = next_node
        self._head = prev

    def compare(self, other):
        current1 = self._head
        current2 = other._head
        while current1 and current2:
            if current1._data != current2._data:
                return False
            current1 = current1._next
            current2 = current2._next
        return current1 is None and current2 is None

if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.addToTail(3)
    linked_list.addToHead(6)
    linked_list.addAfter(linked_list._head, 2)
    linked_list.addToHead(1)
    linked_list.addToTail(5)
    linked_list.addAfter(linked_list._head,5)
    linked_list.print_list()

    linked_list.deleteFromHead()
    linked_list.deleteFromTail()
    linked_list.deleteAfter(linked_list._head)
    print("danh sách sau khi xóa")
    linked_list.traverse()

    linked_list.delByValue(2)
    print("Danh sách sau khi xóa phần tử có giá trị 2:")
    linked_list.print_list()

    node = linked_list.search(5)
    if node:
        print("Tìm thấy phần tử:", node.data)
    else:
        print("Không tìm thấy phần tử.")

    print("Số lượng phần tử trong danh sách:", linked_list.count())

    linked_list.deleteAtIndex(0)
    print("Danh sách sau khi xóa phần tử tại chỉ số 0:")
    linked_list.print_list()

    linked_list.insert(4)
    print("Danh sách sau khi thêm 4 vào danh sách đã sắp xếp:")
    linked_list.print_list()

    print("Danh sách có sắp xếp không:", linked_list.is_sorted())

    linked_list.reverse()
    print("Danh sách sau khi đảo ngược:")
    linked_list.print_list()

    print("max", linked_list.max())
    print("min", linked_list.min())
    print("avg", linked_list.avg())
    print("sum", linked_list.sum())
    
    another_list = SinglyLinkedList()
    another_list.addToTail(3)
    another_list.addToHead(1)
    another_list.addToTail(5)
