class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        def __init__(self, el):
            """Default constructor of Node
            """
            self.el = el
            self.next = None
            self.prev = None
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
    def __len__(self):
        return self.size

    def is_empty(self):
        return self.__len__() == 0

    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        newnode = self.Node(data)
        if self.is_empty():
            self.head = newnode
            self.tail = newnode
            self.size += 1
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
            self.size += 1
        # 
        # You code here!
        #
    
    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = self.head.el
        # You code here!
        # 
        return first_data

    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        newnode = self.Node(data)
        if self.is_empty():
            self.head = newnode
            self.tail = newnode
            self.size += 1
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode
            self.size += 1
        # 
        # You code here!
        #
        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = self.tail.el
        # You code here!
        return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        elif self.__len__() == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            current = self.head.next
            self.head = current
            current.prev = None
            self.size -= 1

        # 
        # You code here!
        #
    
    def delete_second(self):
        """Delete the second node
        """
        if self.is_empty() or self.__len__() == 1:
            raise RuntimeError("INVALID REQUEST!")
        elif self.__len__() == 2:
            self.tail = self.head
            self.head.prev = None
            self.tail.next = None
            self.size -= 1
        else:
            current = self.head.next.next
            self.head.next = current
            current.prev = self.head
            self.size -= 1


        # 
        # You code here!
        #
    
    def delete_last(self):
        """Delete the last node
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        elif self.__len__() == 1:
            self.head = None
            self.tail = None
            self.size = 0
        else:
            current = self.tail.prev
            current.next = None
            self.tail = current
            self.size -= 1

        # 
        # You code here!
        #
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.is_empty() or self.__len__() == 1:
            raise RuntimeError("INVALID REQUEST!")
        elif self.__len__() == 2:
            self.head = self.tail
            self.tail.next = None
            self.head.prev = None
            self.size = 1
        else:
            current = self.tail.prev.prev
            current.next = self.tail
            self.tail.prev = current
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
        if self.is_empty():
            return result
        else:
            current = self.head
            result.append(current.el)
            while current.next:
                current = current.next
                result.append(current.el)
        # You code here!
        # 
        return result

    
    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.
        
        Returns:
            A list of all the nodes' data in Linked list from tail to head. 
        """
        
        result = []
        if self.is_empty():
            return result
        else:
            current = self.tail
            result.append(current.el)
            while current.prev:
                current = current.prev
                result.append(current.el)
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



