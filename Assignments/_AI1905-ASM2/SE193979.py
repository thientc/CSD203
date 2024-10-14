class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """

    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        __slots__ = '_element', '_next', '_prev'

        def __init__(self, element):
            """Default constructor of Node
            """
            self._element = element
            self._next = None
            self._prev = None

    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self._head = None
        self._tail = None

    def insert_first(self, data: any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node

    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        if self._head:
            first_data = self._head._element
        return first_data

    def insert_last(self, data: any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail._next = new_node
            new_node._prev = self._tail
            self._tail = new_node

    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        if self._tail:
            last_data = self._tail._element
        return last_data

    def delete_first(self):
        """Delete the first node
        """
        if not self._head:
            raise NameError("The list is empty")
        element = self._head._element
        self._head = self._head._next
        if self._head:
            self._head._prev = None
        else:
            self._tail = None
        return element

    def delete_second(self):
        """Delete the second node
        """
        if not self._head or not self._head._next:
            raise NameError("There is no second node to delete")
        second_node = self._head._next
        self._head._next = second_node._next
        if second_node._next:
            second_node._next._prev = self._head
        else:
            self._tail  =self._head
        return second_node._element

    def delete_last(self):
        """Delete the last node
        """
        if not self._head:
            raise NameError("The list is empty")
        if not self._head._next:
            element = self._head
            self._head = None
            return element
        current = self._head
        while current._next._next:
            current = current._next
        element = current._next._element
        current._next = None
        return element

    def delete_before_last(self):
        """Delete the node before the last one
        """
        if not self._tail or not self._tail._prev:
            raise NameError("There is no node before last to delete")
        before_last = self._tail._prev
        if before_last._prev:
            before_last._prev._next = self._tail
            self._tail._prev = before_last._prev
        else:
            self._head = self._tail
            self._head._next = None
        return before_last._element

    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list


        Returns:
            A list of all the nodes' data in Linked list from head to tail.
        """

        result = []
        current = self._head
        while current:
            result.append(current._element)
            current = current._next
        return result

    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.

        Returns:
            A list of all the nodes' data in Linked list from tail to head.
        """

        result = []
        current = self._tail
        while current:
            result.append(current._element)
            current = current._prev
        return result

    def example_invalid(self):
        """This is an example to handle invalid request

        Raises:
            RuntimeError: raise this error when the request is invalid.
        """
        raise RuntimeError("INVALID REQUEST!")


if __name__ == "__main__":
    mylist = DoublyLinkedList()
    #mylist.insert_first(2)
    #mylist.insert_first(1)
    #mylist.insert_last(3)
    mylist.delete_second()
    result = mylist.list_from_head()
    print(result)
    # result == [1,2,3]