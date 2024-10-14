class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        def __init__(self, data, prev=None, next=None ):
            """Default constructor of Node
            """
            pass
            # 
            # You code here!
            #
            self.data = data
            self.next = next
            self.prev = prev

    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        pass
        # 
        # You code here!
        #
        self.head = self.Node(None)
        self.tail = self.Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head 
        self.size = 0
        

    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        pass
        # 
        # You code here!
        #
        new = self.Node(data)
        new.next = self.head.next
        new.prev = self.head
        self.head.next.prev = new
        self.head.next = new
        self.size += 1

    def show_first(self) -> any:
        """Show only data of the first node-

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        # 
        # You code here!
        # 
        if self.size == 0: 
            raise Exception("NULL")
        first_data = self.head.next.data

        return first_data
    def display(self):
        """Display all data from head to tail"""
        cur = self.head.next
        while cur != self.tail:
            print(cur.data, end=" ")
            cur = cur.next
        print()
    
    def insert_last(self, data:any = None):  #
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        pass
        # 
        # You code here!
        #
        new= self.Node(data)
        new.prev = self.tail.prev
        new.next = self.tail
        self.tail.prev.next = new
        self.tail.prev = new
        self.size += 1
        
    def show_last(self):  #
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        # 
        # You code here!
        # 
        if self.size == 0: 
             raise RuntimeError("INVALID REQUEST!")
        last_data = self.tail.prev.data
        return last_data
    
    def delete_first(self):  #
        """Delete the first node
        """
        pass
        # 
        # You code here!
        #
        if self.size == 0:  raise RuntimeError("INVALID REQUEST!")
        else: 
            self.head.next = self.head.next.next
        self.size -= 1

    
    def delete_second(self):  #
        """Delete the second node
        """
        pass
        # 
        # You code here!
        #
        if self.size == 0:  raise RuntimeError("INVALID REQUEST!")
        else: 
            i = 0 
            while i == 3: 
                i+= 1 
                self.head = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
                


    def delete_last(self):
        """Delete the last node
        """
        pass
        # 
        # You code here!
        #
        if self.size == 0:  raise RuntimeError("INVALID REQUEST!")
        last_node = self.tail.prev
        self.tail.prev = last_node.prev
        last_node.prev.next = self.tail
        self.size -= 1

    def delete_before_last(self):
        """Delete the node before the last one
        """
        pass
        # 
        # You code here!
        #
        if self.size == 0:  raise RuntimeError("INVALID REQUEST!")
    
    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list
        
        
        Returns:
            A list of all the nodes' data in Linked list from head to tail. 
        """
        
        result = []
        # 
        # You code here!
        # 
        if self.size == 0:  raise RuntimeError("INVALID REQUEST!")
        else: 
            cur = self.head.next
            while cur != self.tail :
                result.append(cur.data)
                cur = cur.next

        return result

    
    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.
        
        Returns:
            A list of all the nodes' data in Linked list from tail to head. 
        """
        
        result = []
        # 
        # You code here!
        #
        if self.size == 0:  raise RuntimeError("INVALID REQUEST!")
        else: 
            cur = self.tail.prev
            while cur != self.head :
                result.append(cur.data)
                cur = cur.prev

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