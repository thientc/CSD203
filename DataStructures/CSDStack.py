'''
Stacks are the simplest of all data structures, yet they are also among the most important. They are used in a host of different applications, and as a tool for many more sophisticated data structures and algorithms. 
    S.push(e): Add element e to the top of stack S.
    S.pop(): Remove and return the top element from the stack S; an error occurs if the stack is empty. 
    S.top(): Return a reference to the top element of stack S, without removing it; an error occurs if the stack is empty.
    S.is empty(): Return True if stack S does not contain any elements. 
    len(S): Return the number of elements in stack S.
'''
class CSDStack:
    """ Implementing a Stack Using a Python List """
    def __init__(self) -> None:
        '''Create an empty stack.'''
        self._data = []

    def len(self):
        '''Returns the number of elements in the stack.'''
        return len(self._data)
    
    def push(self, el):
        self._data.append(el)

    def is_empty(self):
        return len(self._data) == 0
    
    def top(self):
        if self.is_empty():
            raise Exception("CSD Stack is empty!")
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Exception("CSD Stack is empty!")
        return self._data.pop()
    
    def remove(self):
        if not self.is_empty():
            self.pop()
            self.remove()

if __name__ == "__main__":
    stack = CSDStack()
    print(stack.is_empty())
    stack.push(9)
    stack.push(8)
    stack.push(7)
    # print(stack.is_empty())
    print(stack.len())
    # print(stack.top())
    stack.remove()
    print(stack.len())
