class CSDLinkedList:
    class CSDNode:
        def __init__(self, el) -> None:
            self.el = el
            self.next = None
    def __init__(self) -> None:
        self.head = None
        # self.tail = None
        # self.size = 0
    
    def insert_to_head(self, el):
        node = self.CSDNode(el)
        node.next = self.head
        self.head = node

    def delete_from_head(self):
        if self.head == None:
            Exception("Linked list is empty!")
        el = self.head.el
        self.head = self.head.next
        return el

if __name__ == "__main__":
    mylist = CSDLinkedList()
    mylist.insert_to_head(4)
    # print(id(mylist.head))
    mylist.insert_to_head(5)
    # print(id(mylist.head))
    mylist.insert_to_head(6)
    # print(id(mylist.head))
    mylist.insert_to_head(7)
    # print(id(mylist.head))
    mylist.insert_to_head(8)
    # print(id(mylist.head))

    print(mylist.delete_from_head())
    print(mylist.delete_from_head())
    print(mylist.delete_from_head())