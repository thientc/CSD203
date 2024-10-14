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
            self.next = None

    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self.head = None

    
    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """

        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        if not self.head:
            raise RuntimeError("INVALID REQUEST!")
        first_data = self.head.data
        return first_data
    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        current = self.head
        while current.next:
            current = current.next
        last_data = current.data
        return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        if not self.head:
            raise RuntimeError("INVALID REQUEST!")
        current = self.head
        self.head = self.head.next
    def delete_second(self):
        """Delete the second node
        """
        if not self.head.next:
            raise RuntimeError("INVALID REQUEST!")
        current = self.head.next
        self.head.next = self.head.next.next
    
    def delete_last(self):
        """Delete the last node
        """
        if not self.head:
            raise RuntimeError("INVALID REQUEST!")
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if not self.head.next:
            raise RuntimeError("INVALID REQUEST!")
        current = self.head
        while current.next.next:
            current = current.next
        node_last = current.next
        current.next = None
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
        self.insert_last(node_last.data)


    
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
        result2 = []
        current = self.head
        while current:
            result2.append(current.data)
            current = current.next
        while result2 != []:
            result.append(result2[-1])
            result2.pop(-1)
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
    mylist.insert_last(5)
    mylist.insert_last(7)
    mylist.delete_before_last()
    mylist.delete_second()
    result = mylist.list_from_tail()
    print(mylist.show_first(), mylist.show_last())
    print(result)
    # result == [1,2,3]