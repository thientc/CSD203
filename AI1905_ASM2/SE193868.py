class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        def __init__(self):
            """Default constructor of Node
            """
            self.data = 0
            self.prev = None
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
        new_node = self.Node()
        new_node.data = data
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        if self.head:
            first_data = self.head.data
        return first_data

    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node()
        new_node.data = data
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        if current.next is None:
            current.next = new_node
            new_node.prev = current

    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        current = self.head
        if current:
            while current.next:
                current = current.next
            last_data = current.data
        return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        if self.head is None:
            print('List empty')
            return
        if self.head.next:
            self.head.next.prev = None
        self.head = self.head.next

    def delete_second(self):
        """Delete the second node
        """
        if not self.head or not self.head.next:
            return
        second_node = self.head.next
        if second_node.next:
            second_node.next.prev = self.head
        self.head.next = second_node.next

    def delete_last(self):
        """Delete the last node
        """
        if self.head is None:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next:
            current = current.next
        current.prev.next = None
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if not self.head or not self.head.next:
            return
        current = self.head
        if not current.next.next:
            self.delete_first()
            return
        while current.next.next:
            current = current.next
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
    
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
        last = self.head
        while last and last.next:
            last = last.next
        while last:
            result.append(last.data)
            last = last.prev
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