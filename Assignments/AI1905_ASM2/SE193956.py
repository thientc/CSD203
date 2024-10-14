class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        def __init__(self, data = None):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    
    def insert_first(self, data:any = None):
        new_node = self.Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def show_first(self) -> any:
        if self.head:
            print(self.head.data)
        return None

    
    def insert_last(self, data:any = None):
        new_node = self.Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        if self.tail:
            print(self.tail.data)
        return None

    def delete_first(self):
        """Delete the first node
        """
        if self.head is None:
            return None
        current = self.head
        self.head = self.head.next
        return current.data

    def delete_second(self):
        """Delete the second node
        """
        if self.head is None or self.head.next is None:
            return
        nut2 = self.head.next
        if nut2 == self.tail:
            self.tail = self.head
            self.head.next = None
        else:
            self.head.next = nut2.next
            nut2.next.prev = self.head

    def delete_last(self):
        """Delete the last node
        """
        if self.tail is None:
            return None
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None



    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.head == self.tail.prev:
            return None
        if self.tail is None or self.tail.prev is None or self.tail.prev == self.head:
            return None
        current = self.tail.prev
        current.prev.next = self.tail
        self.tail.prev = current.prev


    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list
        Returns:
            A list of all the nodes' data in Linked list from head to tail.
        """

        result = []
        if self.head is None:
            return
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.

        Returns:
            A list of all the nodes' data in Linked list from tail to head.
        """

        result = []
        if self.head is None:
            return
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result[::-1]

    def example_invalid(self):
        """This is an example to handle invalid request

        Raises:
            RuntimeError: raise this error when the request is invalid.
        """
        if self.head is None:
            raise RuntimeError("INVALID REQUEST!")
    
if __name__ == "__main__":
    mylist = DoublyLinkedList()
    mylist.insert_first(2)
    mylist.insert_first(1)
    mylist.insert_last(3)
    # mylist.show_first()
    # mylist.show_last()
    # mylist.delete_first()
    # mylist.delete_second()
    # mylist.delete_last()
    # mylist.delete_before_last()





    result = mylist.list_from_head()

    # result == [1,2,3]