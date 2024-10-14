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
            self.data = data
            self.next = None
            self.prev = None
        
    def __init__(self):
        """Default constructor of DoublyLinkedList
        """
        self.head = None
        self.tail = None 
    
    def insert_first(self, data: any = None):
        """Create a new node with data and insert it as the first node

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
    
    def show_first(self) -> any:
        """Show only data of the first node

        Returns:
            any: The data of the first node or None if the list is empty.
        """
        first_data = None
        if self.head:
            return self.head.data
        return first_data
    
    def insert_last(self, data: any = None):
        """Create a new node with data and insert it as the last node

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
                
    def show_last(self) -> any:
        """Show only data of the last node

        Returns:
            any: The data of the last node or None if the list is empty.
        """
        last_data = None
        if self.tail:
            return self.tail.data
        return last_data
    
    def delete_first(self):
        """Delete the first node
        """
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def delete_second(self):
        """Delete the second node
        """
        if not self.head or not self.head.next:
            return
        second_node = self.head.next
        self.head.next = second_node.next
        if second_node.next:
            second_node.next.prev = self.head
        else:
            self.tail = self.head
    
    def delete_last(self):
        """Delete the last node
        """
        if not self.tail:
            return 
        if self.head == self.tail:
            self.head = self.tail = None  
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    def delete_before_last(self):
        """Delete the node before the last one
        """
        if not self.tail or not self.tail.prev:
            return 
        node_before_last = self.tail.prev
        if node_before_last == self.head:
            self.delete_first()
        else:
            node_before_last.prev.next = self.tail
            self.tail.prev = node_before_last.prev
    
    def list_from_head(self) -> list:
        """Traverse from the head and write the visited node's data into a list
        
        Returns:
            list: A list of all the nodes' data in Linked list from head to tail. 
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def list_from_tail(self) -> list:
        """Traverse from the tail and write the visited node's data into a list.
        
        Returns:
            list: A list of all the nodes' data in Linked list from tail to head. 
        """
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result
    
    def example_invalid(self):
        """This is an example to handle invalid request

        Raises:
            RuntimeError: raise this error when the request is invalid.
        """
        raise RuntimeError("INVALID REQUEST!")
    
    def print_list(self):
        """In danh sách liên kết từ đầu đến cuối.
        """
        current = self.head
        while current:
            print(current.data, end=" > " if current.next else "\n")
            current = current.next
            
if __name__ == "__main__":
    mylist = DoublyLinkedList()
    mylist.insert_first(2)
    mylist.insert_first(1)
    mylist.insert_last(3)
    result = mylist.list_from_head()
    # result == [1,2,3]
    
    
    
    

