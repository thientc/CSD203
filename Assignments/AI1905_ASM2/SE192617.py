class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """

    class Node:
        """ Definition of nodes in DoublyLinkedList
        """

        def __init__(self, value):
            """Default constructor of Node
            """
            self.data = value
            self.next = None
            self.prev = None

    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self.head = None
        self.tail = None

    def insert_first(self, data: any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        if self.head is not None:
            first_data = self.head.data
            return first_data
        raise RuntimeError("INVALID REQUEST!")

    def insert_last(self, data: any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        if self.head is not None:
            last_data = self.tail.data
            return last_data
        raise RuntimeError("INVALID REQUEST!")

    def delete_first(self):
        """Delete the first node
        """
        if self.head is None:
            raise RuntimeError("INVALID REQUEST!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_second(self):
        """Delete the second node
        """
        if self.head is None:
            raise RuntimeError("INVALID REQUEST!")
        elif self.head == self.tail:
            raise RuntimeError("INVALID REQUEST!")
        else:
            tmp = self.head.next
            if tmp == self.tail:
                self.delete_last()
            else:
                self.head.next = tmp.next
                tmp.next.prev = self.head

    def delete_last(self):
        """Delete the last node
        """
        if self.head is None:
            raise RuntimeError("INVALID REQUEST!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.head is None:
            raise RuntimeError("INVALID REQUEST!")
        elif self.head == self.tail:
            raise RuntimeError("INVALID REQUEST!")
        else:
            tmp = self.tail.prev
            if tmp == self.head:
                self.delete_first()
            else:
                self.tail.prev = tmp.prev
                tmp.prev.next = self.tail

    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list


        Returns:
            A list of all the nodes' data in Linked list from head to tail.
        """

        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        if len(result) == 0:
            raise RuntimeError("INVALID REQUEST!")
        else:
            return result

    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.

        Returns:
            A list of all the nodes' data in Linked list from tail to head.
        """

        result = []
        curr = self.tail
        while curr:
            result.append(curr.data)
            curr = curr.prev
        if len(result) == 0:
            raise RuntimeError("INVALID REQUEST!")
        else:
            return result

    def example_invalid(self):
        """This is an example to handle invalid request

        Raises:
            RuntimeError: raise this error when the request is invalid.
        """
        raise RuntimeError("INVALID REQUEST!")


if __name__ == "__main__":
    mylist = DoublyLinkedList()
    mylist.insert_first(1)
    mylist.insert_first(2)
    mylist.insert_first(3)
    mylist.insert_first(4)
    result = mylist.list_from_head()
    print(result)
