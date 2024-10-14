class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        def __init__(self, data=None, next =None, prev = None) -> None:
            """Default constructor of Node
            """
            self.data = data
            self.next = next
            self.previous = prev

            # 
            # You code here!
            #
        
    def __init__(self) -> None:
        """Default constructor of DoublyLinkedList
        """
        self.head = None
        self.tail = None

        #
        # You code here!
        #
    
    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node
        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # 
        # You code here!
        #

    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        if self.head:
            return self.head.data
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

        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        # 
        # You code here!
        #
        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        if self.tail:
            return self.tail.data
        # 
        # You code here!
        # 
        return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        if self.head is None:
            raise RuntimeError("INVALID REQUEST!")
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        # 
        # You code here!
        #
    
    def delete_second(self):
        """Delete the second node
        """
        if self.head is None or self.head.next is None:
            raise RuntimeError("INVALID REQUEST!")

        # 
        # You code here!
        #
    
    def delete_last(self):
        """Delete the last node
        """
        if self.tail is None:
            raise RuntimeError("INVALID REQUEST!")

        if self.tail:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        # 
        # You code here!
        #
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.head is None or self.head.next is None:
            raise RuntimeError("INVALID REQUEST!")

        # 
        # You code here!
        #
    
    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list
        
        
        Returns:
            A list of all the nodes' data in Linked list from head to tail. 
        """
        result = []
        added_head = self.head
        while added_head:
            result.append(added_head.data)
            added_head = added_head.next
        return result

        # 
        # You code here!
        # 


    
    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.
        
        Returns:
            A list of all the nodes' data in Linked list from tail to head. 
        """
        
        result = []
        added_tail = self.tail
        while added_tail:
            result.append(added_tail.data)
            added_tail = added_tail.prev
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
    mylist.insert_first(2)
    mylist.insert_first(1)
    mylist.insert_last(3)
    result = mylist.list_from_head()
    # result == [1,2,3]


