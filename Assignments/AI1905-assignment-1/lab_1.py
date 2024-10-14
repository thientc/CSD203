#Question 1:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def addToHead(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode
        self._size+=1
    def addTotail(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            self._size+=1
        else:
            current = self.head
            while current.next:
                current = current.next
            newnode.next = current.next
            current.next = newnode
            self._size+=1
    def addAfter(self,p,x):
        newnode = Node(x)
        current= self.head

        while current.next:
            if current.data == p:
                newnode.next=current.next
                current.next=newnode
                self._size+=1
            current = current.next

    def travesal(self):
        current = self.head
        while current != None:
            print(current.data, '-> ',end='')
            current = current.next
    def deleteFromHead(self, data):
        if self.head == None:
            print('List is empty')
            return
        else:
            self.head = self.head.next
    def deleteFromTail(self):
        if self.head == None:
            print('List is empty')
            return
        if self.head.next == None:
            self.head = None
            return
        current = self.head
        while current.next.next :
            current = current.next
        current.next = None
    def deleteAfter(self,p):
        current = self.head
        while current.next:
            if current.data == p:
                current.next=current.next.next
                return p
            current = current.next
        print('Invalid')
    def del_value_x(self,x):
        current = self.head
        while current.next:
            if current.next.data == x:
                current.next = current.next.next
                return x
            current = current.next
        print('invalid')
    def search(self,x):
        count = 0
        current = self.head
        while current != None:
            if current.data == x:
                return count
            count += 1
            current = current.next
    def count(self):
        count=1
        current = self.head
        while current.next:
            count+=1
            current = current.next
        return count
    def del_i_th_node(self,i):
        current = self.head
        count = 0
        if current == None:
            print('invalid')
        else:
            while current.next:
                if i==0:
                    self.head = self.head.next
                if count == i-1:
                    current.next= current.next.next
                count+=1
                current=current.next
    def sort(self):
        list_ = []
        current = self.head
        list_.append(current.data)
        while current.next:
            current = current.next
            list_.append(current.data)
        list_.sort()
        print(list_)
        current = self.head
        for i in range(0,len(list_)):
            if i == len(list_):
                current.data = list_[i]
            else:
                current.data = list_[i]
                current= current.next
    def del_nodep(self,p):
        current = self.head
        while current.next:
            if current.next.data == p:
                current.next = current.next.next
                continue
            current = current.next
        print('invalid')


myList = SinglyLinkedList()
myList.addToHead(10)
myList.addToHead(30)
myList.addToHead(40)
myList.addTotail(20)
print(myList.travesal())
myList.deleteAfter(70)
print(myList.travesal())
myList.del_value_x(30)
print(myList.travesal())
myList.addAfter(10,90)
print(myList.travesal())
print(myList.search(10))
print(myList.travesal())
print(myList.count())
myList.addToHead(10)
myList.addToHead(30)
myList.addToHead(40)
myList.addTotail(20)
print(myList.travesal())
myList.del_i_th_node(1)
print(myList.travesal())
myList.sort()
print(myList.travesal())