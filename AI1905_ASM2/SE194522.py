class DoublyLinkedList:
    class Node:
        def __init__(self,data=None):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self, data: any = None):
        new_node = self.Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def show_first(self) -> any:

        first_data = None
        if self.head is not None:
            first_data = self.head.data
        return first_data

    def insert_last(self, data: any = None):
        new_node = self.Node(data)
        if self.tail == None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def show_last(self):
        """Show only data of the last node

        Args:
            data (any, optional): The node data. Defaults to None.
        """
        last_data = None
        if self.tail is not None:
            last_data = self.tail.data
        return last_data

    def delete_first(self):
        if self.head == None:
            raise RuntimeError('Lỗi nhóe!!!!')
        if self.head == self.tail:
            self.head = self.tail = None

    def delete_second(self):
        if self.head == None or self.head.next == None:
            raise RuntimeError('Lỗi rồi đm!!!!')
        second_node = self.head.next
        if second_node == self.tail:
            self.tail = self.head
            self.head.next = None
        else:
            self.head.next = second_node.next
            second_node.next.prev = self.head

    def delete_last(self):
        if self.tail == None:
            raise RuntimeError('Sai nhe kekekeke')
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def delete_before_last(self):
        if self.tail == None or self.tail.prev == None:
            raise RuntimeError('Khựa khựa ngu chưa!')
        before_last = self.tail.prev
        if before_last == self.head:
            self.head = self.tail
            self.head.next = None
        else:
            before_last.prev.next = self.tail
            self.tail.prev = before_last.prev

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
    mylist.insert_last(3)
    result = mylist.list_from_head()
    # result == [1,2,3]