class Node:
            def __init__(self, element):
                self._element = element
                self.next = None
                


class SinglyLinkedList: 
    
    def __init__(self):
         self.head = None
         self.next = None 

    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node


    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node

    def addAfter(self, p:Node, x):
        new_node = Node(x)
        if p is None:
            return 
        else:
             new_node.next = p.next
             p.next = new_node
    
    def traverse(self):
        cur_node = self.head
        while cur_node:
            print(cur_node._element, end=" ")
            cur_node = cur_node.next

    def deleteFromHead(self):
        answer = self.head._element
        self.head = self.head.next
        return answer
    
    def deleteFromTail(self):
        cur_node = self.head
        while cur_node.next.next:
            cur_node = cur_node.next
        answer = cur_node.next._element
        cur_node.next = None
        return answer

    def deleteAter(self, p:Node):
        if not p:
            return
        if not p.next:
            return 
        answer = p.next._element
        p.next = p.next.next
        return answer
    
    def delete_x (self, x):
        if not self.head._element == x:
            return 
        if self.head._element == x:
            return SinglyLinkedList.deleteFromHead()
        cur_node = self.head
        while cur_node.next and cur_node.next._element != x:
                cur_node = cur_node.next
        cur_node.next = cur_node.next.next

    def search_x(self, x):
        pass

    def count(self):
        cur_node = self.head
        count = 0
        while cur_node:
             count +=1 
             cur_node = cur_node.next 
        return count
    
    def delete_nth (self, n):
        pass

    def sort(self):
        if not self.head:
            return
        if not self.head.next:
            return self.head._element
        cur_node = self.head
        while cur_node:
            next_node = cur_node.next
            while next_node:
                if cur_node._element > next_node._element:
                    cur_node._element, next_node._element = next_node._element, cur_node._element
                next_node = next_node.next
            cur_node = cur_node.next
