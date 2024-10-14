class DoublyLinkedList:
    """DoublyLinkedList template for CSD203 assessment

    Raises:
        RuntimeError: _description_
    """
    class Node:
        """ Definition of nodes in DoublyLinkedList
        """
        def __init__(self, data):
            """Default constructor of Node
            """
            self._data = data
            self._next = None
            self._prev = None
        
    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def insert_first(self,data:any = None):
        """Create a new node with data and insert data as the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        if self.is_empty():
            new_node._next = self._head
            self._head = new_node
        else:
            new_node._next = self._head
            self._head._prev = new_node
            self._head = new_node
        self._size += 1
    
    def show_first(self) -> any:
        """Show only data of the first node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        if self.is_empty():
            self.example_invalid()
        first_data = self._head._data
        return first_data
    
    def insert_last(self, data:any = None):
        """Create a new node with data and insert data as the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        new_node = self.Node(data)
        crr = self._head
        if self.is_empty():
            new_node._next = self._head
            self._head = new_node
        else:
            while crr._next is not None:
                crr = crr._next
            crr._next = new_node
            new_node._prev = crr
        self._size += 1
        
    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        if self.is_empty():
            self.example_invalid()
        elif self._size == 1:
            return self._head._data
        else:
            crr = self._head
            while crr._next is not None:
                crr = crr._next
            last_data = crr._data
            return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        if self.is_empty():
            self.example_invalid()
        else:
            self._head = self._head._next

        self._size -= 1
    
    def delete_second(self):
        """Delete the second node
        """
        if self._size < 2:
            self.example_invalid()
        else:
            second_node = self._head._next
            self._head._next = second_node._next
            if second_node._next:
                second_node._next._prev = self._head
            self._size -= 1
    
    def delete_last(self):
        """Delete the last node
        """
        if self.is_empty():
            self.example_invalid()
        if self._size == 1:
            self._head = None
        else:
            crr = self._head
            while crr._next._next is not None:
                crr = crr._next
            crr._next = None
        self._size -= 1
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if self._size < 2:
            self.example_invalid()
        elif self._size == 2:
            self.delete_first()
        else:
            crr = self._head
            while crr._next._next is not None:
                crr = crr._next
            crr._prev._next = crr._next
            crr._next._prev = crr._prev
            self._size -= 1
    
    def list_from_head(self):
        """Traverse from the head and write the visited node's data into a list
        
        
        Returns:
            A list of all the nodes' data in Linked list from head to tail. 
        """
        if self.is_empty():
            self.example_invalid()
        result = []
        crr = self._head
        while crr is not None:
            result.append(crr._data)
            crr = crr._next
        return result
    
    def list_from_tail(self):
        """Traverse from the taile and write the visited node's data into a list.
        
        Returns:
            A list of all the nodes' data in Linked list from tail to head. 
        """
        if self.is_empty():
            self.example_invalid()
        lst = []
        crr = self._head
        while crr is not None:
            lst.append(crr._data)
            crr = crr._next
        return lst[::-1]
    
    def example_invalid(self):
        """This is an example to handle invalid request

        Raises:
            RuntimeError: raise this error when the request is invalid.
        """
        raise RuntimeError("INVALID REQUEST!")

    def traverse(self):
        crr = self._head
        while crr is not None:
            print(crr._data, end=' ')
            crr = crr._next
        print()
if __name__ == "__main__":
    mylist = DoublyLinkedList()
    mylist.insert_first(2)
    mylist.insert_first(1)
    mylist.insert_last(3)
    result = mylist.list_from_head()
    # result == [1,2,3]




