import sys

class DoublyLinkedList:
    __slot__ = "head", "tail", "size"
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        __slot__ = "data", "next", "prev"

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
        node = self.Node(data)
        if self.head is None and self.tail is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        # 
        # You code here!
        #
    
    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        if self.head:
            return self.head.data
        raise RuntimeError("INVALID REQUEST!")
        
    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        node = self.Node(data)
        if self.head is None and self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        if self.head:
            return self.head.data
        raise RuntimeError("INVALID REQUEST!")
    
    def delete_first(self):
        """Delete the first node
        """
        if self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            raise RuntimeError("INVALID REQUEST!")
        # 
        # You code here!
        #
    
    def delete_second(self):
        """Delete the second node
        """
        
        if self.head and self.head.next:
            if self.head.next.next:
                second = self.head.next
                second.next.prev = self.head
                self.head.next = second.next
            else:
                self.tail = self.head
                self.head.next = None
        else:
            raise RuntimeError("INVALID REQUEST!")
        # 
        # You code here!
        #
    
    def delete_last(self):
        """Delete the last node
        """
        if self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            raise RuntimeError("INVALID REQUEST!")
        
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.tail and self.tail.prev:
            if self.tail.prev.prev:
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
            else:
                self.head = self.tail
                self.tail.prev = None
        else:
            raise RuntimeError("INVALID REQUEST!")
    
    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list
        
        
        Returns:
            A list of all the nodes' data in Linked list from head to tail. 
        """
        result = []
        curr = self.head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result

    
    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.
        
        Returns:
            A list of all the nodes' data in Linked list from tail to head. 
        """
        
        result = []
        curr = self.tail
        while curr:
            result.append(curr.data)
            curr = curr.prev
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
    mylist.insert_first(3)
    mylist.delete_second()
    mylist.insert_first(4)
    result = mylist.list_from_head()
    print(result)
    # result == [1,2,3]