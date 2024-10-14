class CSDStack:
    """ comment """
    def __init__(self) -> None:
        self._data = []

    def len(self):
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
