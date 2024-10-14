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
            
            # 
            # You code here!
            self.data = data
            self.next = None
            self.prev = None

            #
        
    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        
        # 
        # You code here!
        self.head = None 
        self.tail = None

        #
    def traverse(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end= '->')
            cur_node = cur_node.next
    
    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        
        # 
        # You code here!
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        #
    
    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        # 
        # You code here!
        if self.head is None:
            raise RuntimeError("INVALID REQUEST!")
        else:
            first_data = self.head.data
        # 
        return first_data

    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        
        # 
        # You code here!
        
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        #
        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        # 
        # You code here!
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        last_data = cur_node.data
        # 
        return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        # 
        # You code here!
        if self.head is None:
            raise RuntimeError("INVALID REQUEST!")
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        #
    
    def delete_second(self):
        """Delete the second node
        """
        
        # 
        # You code here!
        if self.head is None or self.head.next is None:
            raise RuntimeError("INVALID REQUEST!")
        cur_node = self.head.next
        if cur_node.next is None:
            self.tail = self.head
        else:
            cur_node.prev.next = cur_node.next
            cur_node.next.prev = cur_node.prev

        #
    
    def delete_last(self):
        """Delete the last node
        """
        
        # 
        # You code here!
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.prev.next = None
        #
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        
        # 
        # You code here!
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        delete_node = cur_node.prev
        delete_node.prev.next = cur_node


        
        #
    
    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list
        
        
        Returns:
            A list of all the nodes' data in Linked list from head to tail. 
        """
        
        result = []
        # 
        # You code here!
        cur_node = self.head
        while cur_node:
            result.append(cur_node.data)
            cur_node = cur_node.next
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
        cur_node = self.tail
        while cur_node:
            result.append(cur_node.data)
            cur_node = cur_node.prev

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
    mylist.insert_last(2)
    mylist.insert_last(1)
    mylist.insert_last(3)
    mylist.delete_last()
    result = mylist.list_from_head()
    # result = mylist.list_from_tail()
    print(result)
    # result == [1,2,3]

