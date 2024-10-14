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
            self.prev = None
            self.data = data
            self.next = None
            # 
            # You code here!
            #
        
    def __init__(self):
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
        newNode = self.Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        #
        # You code here!
        #
    
    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        if self.head is None:
            raise RuntimeError("INVALID REQUEST!")
        else:
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
        newNode = self.Node(data)
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        # 
        # You code here!
        #
        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        if self.tail is None:
            raise RuntimeError("INVALID REQUEST!")
        else:
            last_data = self.tail.data
        # 
        # You code here!
        # 
        return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        cur = self.head
        if cur is None:
            raise RuntimeError("INVALID REQUEST!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        # 
        # You code here!
        #
    
    def delete_second(self):
        """Delete the second node
        """
        cur = self.head
        if cur.next is None:
            raise RuntimeError("INVALID REQUEST!")
        elif cur.next == self.tail:
            self.delete_last()
        else:
            cur.next = cur.next.next
            cur.next.prev = cur
        #
        # You code here!
        #
    
    def delete_last(self):
        """Delete the last node
        """
        cur = self.tail
        if cur is None:
            raise RuntimeError("INVALID REQUEST!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        # 
        # You code here!
        #
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        cur = self.tail
        if cur.prev is None:
            raise RuntimeError("INVALID REQUEST!")
        elif cur.prev == self.head:
            self.delete_first()
        else:
            cur.prev = cur.prev.prev
            cur.prev.next = cur
        # 
        # You code here!
        #
    
    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list
        
        
        Returns:
            A list of all the nodes' data in Linked list from head to tail. 
        """
        
        result = []
        cur = self.head
        if cur is None:
            raise RuntimeError("INVALID REQUEST!")
        while cur:
            result.append(cur.data)
            cur = cur.next
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
        cur = self.tail
        if cur is None:
            raise RuntimeError("INVALID REQUEST!")
        while cur:
            result.append(cur.data)
            cur = cur.prev
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