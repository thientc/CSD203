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
            pass
            # 
            # You code here!
            self.data = data
            self.prev = None
            self.next = None

            #
        
    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        pass
        # 
        # You code here!
        self.head = None
        self.tail = None
        self.size = 0
        #
    
    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        pass
        # 
        # You code here!
        newNode = self.Node(data)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1


        #
    
    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        # 
        # You code here!
        if self.head:
            first_data = self.head.data
        # 
        return first_data

    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        pass
        # 
        # You code here!
        newNode = self.Node(data)
        if (self.size == 0):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1
        #
        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        # 
        # You code here!
        if self.tail:
            last_data = self.tail.data
        # 
        return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        pass
        # 
        # You code here!
        if (self.size > 1):
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return
        if (self.size < 2):
            self.head = None
            self.tail = None
            self.size = 0
        #
    
    def delete_second(self):
        """Delete the second node
        """
        pass
        # 
        # You code here!
        if self.head is None or self.head.next is None:
            self.example_invalid()
        second_node = self.head.next
        if second_node == self.tail:
            self.delete_last()
        else:
            self.head.next = second_node.next
            second_node.next.prev = self.head
        self.size -= 1
        #
    
    def delete_last(self):
        """Delete the last node
        """
        pass
        # 
        # You code here!
        if (self.size > 1):
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return
        if (self.size < 2):
            self.head = None
            self.tail = None
            self.size = 0
        #
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        pass
        # 
        # You code here!
        if self.tail is None or self.tail.prev is None:
            self.example_invalid()
        if self.tail.prev == self.head:
            self.delete_first()
        else:
            node_before_last = self.tail.prev
            node_before_last.prev.next = self.tail
            self.tail.prev = node_before_last.prev
        self.size -= 1
        #
    
    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list

        
        Returns:
            A list of all the nodes' data in Linked list from head to tail. 
        """
        
        result = []
        # 
        # You code here!
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        # 
        return result

    
    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.
        
        Returns:
            A list of all the nodes' data in Linked list from tail to head. 
        """
        
        result = []
        # 
        # You code here!
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
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
    mylist.insert_first(2)
    mylist.insert_last(3)
    mylist.insert_first(1)
    mylist.insert_last(4)

    result = mylist.list_from_head()
    # result == [1,2,3]
    print(result)
