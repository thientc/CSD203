
class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        def __init__(self, data):
            self.element = data
            self.prev = None
            self.next = None
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
        # 
        # You code here!
        #
    def is_empty(self):
        return self.size == 0

    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        else:
            first_data = self.head.element
            return first_data
        # 
        # You code here!
        # 


    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        # 
        # You code here!
        #
        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        else:
            last_data = self.tail.element
            return last_data
        # 
        # You code here!
        # 

    
    def delete_first(self):
        """Delete the first node
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        elif self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        # 
        # You code here!
        #
    
    def delete_second(self):
        """Delete the second node
        """
        if self.is_empty() or self.size == 1:
            raise RuntimeError("INVALID REQUEST!")
        elif self.size == 2:
            self.tail = self.head
            self.head.next = None
        else:
            self.head.next = self.head.next.next
            self.head.next.prev = self.head
        self.size -= 1
        # 
        # You code here!
        #
    
    def delete_last(self):
        """Delete the last node
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        elif self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        # 
        # You code here!
        #
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        elif not self.tail.prev:
            raise RuntimeError("INVALID REQUEST!")
        elif self.size == 2:
            self.head = self.tail
            self.tail.prev = None
        else:
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
        self.size -= 1
        # 
        # You code here!
        #
    
    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list
        
        
        Returns:
            A list of all the nodes' data in Linked list from head to tail. 
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        else:
            temp = self.head
            result = []
            while temp:
                result.append(temp.element)
                temp = temp.next
            return result
            #
            # You code here!
            #

        # 
        # You code here!


    
    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.
        
        Returns:
            A list of all the nodes' data in Linked list from tail to head. 
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        else:
            temp = self.head
            result = []
            while temp:
                result.append(temp.element)
                temp = temp.next
            result = result[::-1]
            #
            # You code here!
            #
            return result
    
    # def example_invalid(self):
    #     """This is an example to handle invalid request
    #
    #     Raises:
    #         RuntimeError: raise this error when the request is invalid.
    #     """
    #     raise RuntimeError("INVALID REQUEST!")
    
if __name__ == "__main__":
    mylist = DoublyLinkedList()
    mylist.insert_first(2)
    mylist.insert_first(1)
    mylist.insert_last(3)
    mylist.insert_last(6)
    result = mylist.list_from_head()
    # result == [1,2,3]