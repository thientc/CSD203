class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """

    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        def __init__(self, data=None):
            """Default constructor of Node
            """
            self.data = data
            self.prev = None
            self.next = None


    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        #
        # You code here!
        self.head = None
        self.tail = None


    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """

        # 
        # You code here!
        #
        new_node = self.Node(data)
        if not self.head:
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
        # 
        # You code here!
        #
        if not self.head:
            raise RuntimeError("List is empty")
        return self.head.data


    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        # 
        # You code here!
        #
        if not self.tail:
            raise RuntimeError("List is empty")
        return self.tail.data

    
    def delete_first(self):
        """Delete the first node
        """
        if not self.head:
            raise RuntimeError("List is empty")
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def delete_second(self):
        """Delete the second node
        """
        if not self.head or not self.head.next:
            raise RuntimeError("List is empty or has only one node")
        second_node = self.head.next
        if second_node == self.tail:
            self.tail = self.head
        else:
            second_node.prev.next = second_node.next
            second_node.next.prev = second_node.prev


    def delete_last(self):
        """Delete the last node
        """
        if not self.tail:
            raise RuntimeError("List is empty")
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_before_last(self):
        """Delete the node before the last one
        """
        if not self.head or not self.head.next:
            raise RuntimeError("List has fewer than two nodes")
        if self.head.next == self.tail:
            self.head = self.tail  # Only two nodes, so head becomes the tail
            self.head.prev = None
        else:
            node_before_last = self.tail.prev
            node_before_last.prev.next = self.tail
            self.tail.prev = node_before_last.prev
    
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
    # mylist.insert_first(2)
    # mylist.insert_first(1)
    # mylist.insert_last(3)
    # result = mylist.list_from_head()
    # # result == [1,2,3]

    mylist.insert_first(2)
    mylist.insert_first(24)
    mylist.insert_first(3)
    mylist.insert_first('alosde')
    mylist.insert_first('Mi')
    mylist.insert_last('last')
    # mylist.delete_first()
    # mylist.delete_last()
    # mylist.delete_second()


    print(mylist.show_first())

    print(mylist.show_last())
    print(mylist.list_from_tail())
    print(mylist.list_from_head())

