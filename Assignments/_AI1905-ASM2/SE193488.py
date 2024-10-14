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
            self.prev = None

        
    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.size == 0:
            self.head = self.tail = new_node
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
        if self.size == 0:
            return first_data
        else:
            first_data = self.head
        return first_data.data

    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.size == 0:
            self.head = self.tail = new_node
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
        if self.size == 0:
            return last_data
        else:
            last_data = self.tail
        return last_data.data
    
    def delete_first(self):
        """Delete the first node
        """
        if self.size == 0:
            raise RuntimeError("INVALID REQUEST!")
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
    
    def delete_second(self):
        """Delete the second node
        """
        if self.head is None or self.head.next is None:
            raise RuntimeError("INVALID REQUEST!")
        current = self.head.next
        if current == self.tail:
            self.tail = self.head
            self.head.next = None
        else:
            self.head.next = current.next
            current.next.prev = self.head
        self.size -= 1
    
    def delete_last(self):
        """Delete the last node
        """
        pass
        if self.size == 0:
            raise RuntimeError("INVALID REQUEST!")
        if self.size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.head == self.tail.prev:
            raise RuntimeError("INVALID REQUEST!")
        if self.tail is None or self.tail.prev is None or self.tail.prev == self.head:
            raise RuntimeError("INVALID REQUEST!")
        current = self.tail.prev
        current.prev.next = self.tail
        self.tail.prev = current.prev
    
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
    mylist.insert_last(5)
    mylist.insert_first(7)
    mylist.insert_last(6)
    mylist.insert_last(8)
    mylist.insert_first(9)
    mylist.insert_last(4)

    result = mylist.list_from_head()
    print(result)
    result = mylist.list_from_tail()
    print(result)

    print(mylist.show_first())
    print(mylist.show_last())

    mylist.delete_first()
    mylist.delete_last()
    result = mylist.list_from_head()
    print(result)

    mylist.delete_second()
    mylist.delete_before_last()
    result = mylist.list_from_head()
    print(result)
    # result == [1,2,3]