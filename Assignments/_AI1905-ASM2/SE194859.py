class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """

    class Node:
        """ Definition of nodes in DoublyLinkedList
        """

        def __init__(self,data):
            """Default constructor of Node
            """
            self.data = data
            self.next = None
            self.pre = None

    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self.first = None
        self.last = None

    def insert_first(self, data: any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)

        if not self.first:
            self.first = self.last = new_node
        else:
            new_node.next = self.first
            self.first.prev = new_node
            self.first = new_node

    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        if self.first:
            return self.first.data
        return first_data

    def insert_last(self, data: any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if not self.last:
            self.first = self.last = new_node
        else:
            new_node.prev = self.last
            self.last.next = new_node
            self.last = new_node

    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        if self.last:
            return self.last.data
        return last_data

    def delete_first(self):
        """Delete the first node
        """
        if self.first is None:
            Exception("Linked list is empty")
        el = self.first.el
        self.first = self.first.next
        return el

    def delete_second(self):
        """Delete the second node
        """
        if self.first.next is None:
            Exception("Linked list is empty")
        el = self.first.el
        self.first.next = self.first.next.next
        return el

    def delete_last(self):
        """Delete the last node
        """
        if self.last is None:
            Exception("Linked list is empty")
        el = self.last.el
        self.last = self.last.pre
        return el

    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.last.pre is None:
            Exception("Linked list is empty")
        el = self.last.el
        self.last.pre.next = self.last
        return el

    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list


        Returns:
            A list of all the nodes' data in Linked list from head to tail.
        """

        result = []
        temp = self.first
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result

    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.

        Returns:
            A list of all the nodes' data in Linked list from tail to head.
        """

        result = []
        temp = self.last
        while temp:
            result.append(temp.data)
            temp = temp.next
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
