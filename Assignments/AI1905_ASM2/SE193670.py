class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """

        def __init__(self, data=None):
            """Constructor of Node
            """
            self.data = data
            self.next = None
            self.previous = None

    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self.first = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def insert_first(self, data: any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.first is None:
            self.last = new_node
        else:
            new_node.next = self.first
            self.first.previous = new_node
        self.first = new_node
        self.size += 1

    def show_first(self) -> any:
        """Show the data of the first node"""
        if self.first is not None:
            return self.first.data
        return None

    def insert_last(self, data: any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.previous = self.last
            self.last = new_node
        self.size += 1

    def show_last(self):
        """Show the data of the last node"""
        if self.last is not None:
            return self.last.data
        return None

    def delete_first(self):
        """Delete the first node"""
        if self.first is not None:
            self.first = self.first.next
            if self.first is not None:
                self.first.previous = None
            else:
                self.last = None
            self.size -= 1

    def delete_last(self):
        """Delete the last node"""
        if self.last is not None:
            self.last = self.last.previous
            if self.last is not None:
                self.last.next = None
            else:
                self.first = None
            self.size -= 1

    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list

        Returns:
            A list of all the nodes' data in Linked list from head to tail.
        """
        result = []
        current = self.first
        while current:
            result.append(current.data)
            current = current.next
        return result

    def list_from_tail(self):
        """Traverse from the tail and write the visited node's data into a list.

        Returns:
            A list of all the nodes' data in Linked list from tail to head.
        """
        result = []
        current = self.last
        while current:
            result.append(current.data)
            current = current.previous
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