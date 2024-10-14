class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """

    class Node:
        """ Definition of nodes in DoublyLinkedList
        """

        def __init__(self, data):
            """Default constructor of Node
            """
            self.data = data
            self.pre = None
            self.next = None

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
        node = self.Node(data)
        node.next = self.head
        node.pre = None
        if self.head is not None:
            self.head.pre = node
        self.head = node

    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        if self.head is None:
            example_invalid(self)
        first_data = self.head
        return first_data

    def insert_last(self, data: any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new = self.Node(data)
        if self.head is None:
            self.head = new
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new
        new.pre = cur

        new.next = None

    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        last_data = self.head
        if self.head is None:
            example_invalid(self)
        while last_data.next is not None:
            last_data = last_data.next

        return last_data

    def delete_first(self):
        """Delete the first node
        """
        if self.head is None:
            example_invalid(self)
        self.head = None
        self.head.next = self.head

    def delete_second(self):
        """Delete the second node
        """
        pass
        if self.head.next is None:
            example_invalid(self)
        self.head.next = None
        self.head.next.next = self.head.next

    def delete_last(self):
        """Delete the last node
        """
        last_data = self.head
        if self.head is None:
            example_invalid(self)
        while last_data.next is not None:
            last_data = last_data.next
        last_data = None
        last_data.pre = last_data

    def delete_before_last(self):
        """Delete the node before the last one
        """
        last_data.pre = self.head
        if self.head is None:
            example_invalid(self)
        while last_data is not None:
            last_data.pre = last_data.pre.next
        last_data.pre = None
        last_data.pre.pre = last_data.pre

    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list


        Returns:
            A list of all the nodes' data in Linked list from head to tail.
        """

        result = []
        value = self.head
        while value is not None:
            result.append(value)
            value = value.next
        return result

    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.

        Returns:
            A list of all the nodes' data in Linked list from tail to head.
        """

        result = []
        value = self.head
        while value is not None:
            value = value.next
        while value is not None:
            result.append(value)
            value = value.pre

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