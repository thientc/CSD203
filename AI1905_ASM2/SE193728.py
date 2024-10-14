class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        def __init__(self,element,prev,next):
            """Default constructor of Node
            """
            self._element = element
            self._prev = prev
            self._next = next
            #
            # You code here!
            #

    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self._header = self.Node(None,None,None)
        self._trailer = self.Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._next = self._header
        self._size = 0
        # 
        # You code here!
        #

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, data, predecessor, successor):
        new_node = self.Node(data, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element

    def insert_first(self, data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        return self._insert_between(data, self._header, self._header._next)
        # 
        # You code here!
        #
    
    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        if self.is_empty():
            raise Exception("List is empty")
        return self._header._next._element
        #
        # You code here!
        #


    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        return self._insert_between(data, self._trailer._prev, self._trailer)
        # 
        # You code here!
        #


    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        if self.is_empty():
            raise Exception("List is empty")
        return self._trailer._prev._element
        # 
        # You code here!
        #
    
    def delete_first(self):
        """Delete the first node
        """
        if self.is_empty():
            raise Exception("List is empty")
        return self._delete_node(self._header._next)

        # 
        # You code here!
        #
    
    def delete_second(self):
        """Delete the second node
        """
        if self.is_empty():
            raise Exception("List is empty")
        return self._delete_node(self._header._next._next)

        # 
        # You code here!
        #
    
    def delete_last(self):
        """Delete the last node
        """
        if self.is_empty():
            raise Exception("List is empty")
        return self._delete_node(self._trailer._prev)

        # 
        # You code here!
        #
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self.is_empty():
            raise Exception("List is empty")
        return self._delete_node(self._trailer._prev._prev)
        # 
        # You code here!
        #
    
    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list
        
        
        Returns:
            A list of all the nodes' data in Linked list from head to tail. 
        """

        result = []
        current = self._header._next
        while current != self._trailer:
            result.append(current._element)
            current = current._next
        #
        # You code here!
        #
        return result




    def list_from_tail(self):
        """Traverse from the tail and write the visited node's data into a list.
        
        Returns:
            A list of all the nodes' data in Linked list from tail to head. 
        """
        
        result = []
        current = self._trailer._prev
        while current != self._header:
            result.append(current._element)
            current = current._prev
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