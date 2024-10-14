class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: Raises error for invalid operations
    """

    class Node:
        """Definition of nodes in DoublyLinkedList
        """
        def __init__(self, data=None):
            """Constructor of Node

            Args:
                data (any, optional): The data held by the node. Defaults to None.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, data: any = None):
        """Create a new node with data and insert it as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.head is None:  # List is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def show_first(self) -> any:
        """Show only the data of the first node

        Returns:
            any: Data of the first node
        """
        if self.head is None:
            self.example_invalid()
        return self.head.data

    def insert_last(self, data: any = None):
        """Create a new node with data and insert it as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def show_last(self):
        """Show only the data of the last node

        Returns:
            any: Data of the last node
        """
        if self.tail is None:
            self.example_invalid()
        return self.tail.data

    def delete_first(self):
        """Delete the first node
        """
        if self.head is None:
            self.example_invalid()
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def delete_second(self):
        """Delete the second node
        """
        if self.head is None or self.head.next is None:
            self.example_invalid()
        second_node = self.head.next
        if second_node == self.tail:
            self.delete_last()
        else:
            self.head.next = second_node.next
            second_node.next.prev = self.head
        self.size -= 1

    def delete_last(self):
        """Delete the last node
        """
        if self.tail is None:
            self.example_invalid()
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.tail is None or self.tail.prev is None:
            self.example_invalid()
        if self.tail.prev == self.head:
            self.delete_first()
        else:
            node_before_last = self.tail.prev
            node_before_last.prev.next = self.tail
            self.tail.prev = node_before_last.prev
        self.size -= 1

    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list

        Returns:
            list: A list of all the nodes' data in Linked list from head to tail
        """
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def list_from_tail(self):
        """Traverse from the tail and write the visited node's data into a list.

        Returns:
            list: A list of all the nodes' data in Linked list from tail to head
        """
        result = []
        current = self.tail
        while current is not None:
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
    print(result)
