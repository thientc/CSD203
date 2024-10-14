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
            # 
            # You code here!
            #
        
    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self.head = None
        self.tail = None
        self.size = 0
        # 
        # You code here!
        #
    
    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
        return new_node
        # 
        # You code here!
        #
    
    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        if self.head is not None:
            first_data = self.head.data
        # 
        # You code here!
        # 
        return first_data

    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)                                                                                                                          
        if self.head is None:
            return new_node
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur
        self.tail = new_node
        self.size += 1
        return self.head
        # 
        # You code here!
        #
        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        if self.tail is not None:
            last_data = self.tail.data
        # 
        # You code here!
        # 
        return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        if self.head is None: self.example_invalid()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        # 
        # You code here!
        #
    
    def delete_second(self):
        """Delete the second node
        """
        if self.head is None: self.example_invalid()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        second = self.head.next
        self.head.next = second.next
        if second.next:
            second.next.prev = self.head
        self.size -= 1
        # 
        # You code here!
        #
    
    def delete_last(self):
        """Delete the last node
        """
        if self.tail is None: self.example_invalid()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.prev = None
        self.size -= 1
        # 
        # You code here!
        #
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.tail is None: self.example_invalid()
        if self.head == self.tail:
            self.head = None
            self.tail = None
        if self.head.next == self.tail:
            self.delete_first()
        else:
            before_last = self.tail.prev
            before_last.prev.next = self.tail
            self.tail.prev = before_last.prev
        self.size -= 1
        # 
        # You code here!
        #
    
    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list
        
        
        Returns:
            A list of all the nodes' data in Linked list from head to tail. 
        """
        
        result = []
        curr_node = self.head
        while curr_node is not None:
            result.append(curr_node.data)
            curr_node = curr_node.next
        # 
        # You code here!
        # 
        return result

    
    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.
        
        Returns:
            A list of all the nodes' data in Linked list from tail to head. 
        """
        
        result = []
        curr_node = self.tail
        while curr_node is not None:
            result.append(curr_node.data)
            curr_node = curr_node.prev
        # 
        # You code here!
        #
        return result
    
    def example_invalid(self):
        """This is an example to handle invalid request

        Raises:
            RuntimeError: raise this error when the request is invalid.
        """
        raise RuntimeError("INVALID REQUEST!")
    
if __name__ == "__main__":
    mylist = DoublyLinkedList()
    mylist.insert_last(3)
    mylist.insert_last(4)
    mylist.insert_last(5)
    result = mylist.list_from_tail()
    print(result)
    # result == [1,2,3]