import random
class CSDNode:
    __slots__ = "el", "next", "prev", "id"
    def __init__(self, el, next = None, prev= None) -> None:
        self.el = el
        self.next = next
        self.next = prev
        self.id = random.randint(0, 100)

    def __eq__(self, other: object) -> bool:
        return self.el == other.el and self.id == other.id

class CSDDoublyLinkedList:
    def __init__(self) -> None:
        self.head = CSDNode(None, None, None)
        self.tail = CSDNode(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_to_head(self, node:CSDNode):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def insert_to_tail(self, node:CSDNode):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail

    def find_node(self, node:CSDNode):
        cursor = self.head
        while cursor.next:
            cursor = cursor.next
            if cursor == node:
                return True
        return False

if __name__ == "__main__":
    mylist = CSDDoublyLinkedList()
    f = "first"
    node11 = CSDNode(f)
    node12 = CSDNode(f)
    node2 = CSDNode("second")
    node3 = CSDNode("third")
    # # mylist.insert_to_tail(node1)
    # # mylist.insert_to_tail(node2)
    # # mylist.insert_to_tail(node3)
    mylist.insert_to_head(node11)
    mylist.insert_to_head(node2)
    mylist.insert_to_head(node3)
    print(mylist.find_node(node11))
    print(mylist.find_node(node12))

    # # print(mylist.head.next.el)
    # # print(node3.el)
    # node4= CSDNode("fourth")
    # # mylist.insert_after(node3, node4)
    # #     node4.next = node3.next
    # #     node3.next.prev = node4
    # #     node3.next = node4
    # #     node4.prev = node3
    # # mylist.insert_after_node(new_node, cur_node)
    pass
