class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """

        def __init__(self, value):
            self.data = value
            self.next = None
            self.prev = None
    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        #
        # You code here!

        self.head = None
        self.tail = None
        self.size = 0
    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        #
        # You code here!
        #
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        if self.head is not None:
            first_data = self.head.data
        return first_data


    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        #
        # You code here!
        new_node = self.Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        if self.tail is not None:
            last_data = self.tail.data
        return last_data
    def delete_first(self):
        """Delete the first node
        """
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
    def delete_second(self):
        """Delete the second node
        """
        pass
    def delete_last(self):
        """Delete the last node
        """
        if self.tail is None:
            return
        if self.tail == self.head:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

        #
        # You code here!
        #

    def delete_before_last(self):
        if self.tail is None or self.tail.prev is None:
            raise RuntimeError("Loi roi")
        bf = self.tail.prev
        if bf == self.head:
                self.head = self.tail
                self.head.prev = None
        else:
            bf.prev.next = self.tail
            self.tail.prev = bf.prev

        #
        # You code here!
        #

    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list


        Returns:
            A list of all the nodes' data in Linked list from head to tail.
        """

        result = []
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
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result

    def example_invalid(self):
        """This is an example to handle invalid request

        Raises:
            RuntimeError: raise this error when the request is invalid.
        """
        raise RuntimeError("INVALID REQUEST!")
if __name__ == "__main__":
    mylist = DoublyLinkedList()
    mylist.insert_first(2)
    mylist.insert_first(1)
    mylist.insert_last(3)
    result = mylist.list_from_head()
    # result == [1,2,3]