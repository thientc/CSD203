class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        def __init__(self,element):
            """Default constructor of Node
            """
            self.element = element
            self.next = None
            self.pre = None


    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def len(self):
        return self.size
    def is_empty(self):
        return self.len()==0
    
    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        newnode = self.Node(data)
        if self.is_empty():
            self.head = newnode
            self.tail = newnode
        else:
            self.head.pre = newnode
            newnode.next= self.head
            self.head = newnode
        self.size+=1
    
    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        first_data = None
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        else:
            first_data = self.head.element
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
        else:
            self.tail.next = newnode
            newnode.pre = self.tail
            self.tail = newnode
        self.size +=1
        # 
        # You code here!
        #
        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        else:
            last_data = self.tail.element
            return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        else:
            self.head = self.head.next
            self.size-=1

        # 
        # You code here!
        #
    
    def delete_second(self):
        """Delete the second node
        """
        if self.is_empty() or self.len()==1:
            raise RuntimeError("INVALID REQUEST!")
        elif self.len() == 2:
            self.tail = self.tail.pre
            self.size -=1
        else:
            current = self.head
            for i in range(2):
                current = current.next
            current.pre = self.head
            self.head.next = current
            self.size -=1
        # You code here!
        #
    
    def delete_last(self):
        """Delete the last node
        """
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        else:
            self.tail = self.tail.pre
            self.tail.next = None
            self.size-=1
        # 
        # You code here!
        #
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.is_empty() or self.len()==1:
            raise RuntimeError("INVALID REQUEST!")
        elif self.len()==2:
            self.head = self.head.next
            self.size -=1
        else:
            current = self.head
            while current.next.next:
                current = current.next
            self.tail.pre = current.pre
            current.pre.next = self.tail
            

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
            raise RuntimeError("INVALID REQUEST!")
        else:
            result.append(self.head.element)
            current = self.head
            while current.next:
                current = current.next
                result.append(current.element)
        
        return result

    
    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.
        
        Returns:
            A list of all the nodes' data in Linked list from tail to head. 
        """
        
        result = []
        if self.is_empty():
            raise RuntimeError("INVALID REQUEST!")
        else:
            result.append(self.head.element)
            current = self.head
            while current.next:
                current = current.next
                result.append(current.element)

        return result[::-1]
    
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
    mylist.insert_first(2)
    mylist.insert_first(1)

    mylist.delete_last()
    print(mylist.show_last())
    result = mylist.list_from_head()
    print(result)
    # result == [1,2,3]