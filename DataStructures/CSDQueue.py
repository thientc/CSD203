'''
Formally, the queue abstract data type defines a collection that keeps objects in a sequence, where element access and deletion are restricted to the first element in the queue, and element insertion is restricted to the back of the sequence. This restriction enforces the rule that items are inserted and deleted in a queue accord- ing to the first-in, first-out (FIFO) principle.
    Q.enqueue(e): Add element e to the back of queue Q. 
    Q.dequeue(): Remove and return the first element from queue Q; an error occurs if the queue is empty.
    Q.first(): Return a reference to the element at the front of queue Q, without removing it; an error occurs if the queue is empty.
    Q.is empty(): Return True if queue Q does not contain any elements.
    len(Q): Return the number of elements in queue Q; 
'''

class CSDQueueArray:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * CSDQueueArray.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Exception('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Exception('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self.data))     # double the array size
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned

class CSDQueueList:
    """ Implementing a Queue Using a Python List """
    def __init__(self) -> None:
        '''Create an empty queue.'''
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def len(self):
        '''Returns the number of elements in the stack.'''
        return len(self._data)
    
    def enqueue(self, el):
        self._data.append(el)

    def dequeue(self):
        if self.is_empty():
           Exception("CSD Queue is empty!")
        self._data.pop(0)

    def first(self):
        if self.is_empty():
            raise Exception("CSD Queue is empty!")
        return self._data[0]
    
    def remove(self):
        if not self.is_empty():
            self.dequeue()
            self.remove()

if __name__ == "__main__":
    queue = CSDQueueList()
    print(queue.is_empty())
    queue.enqueue(9)
    queue.enqueue(8)
    queue.enqueue(7)
    # print(stack.is_empty())
    print(queue.len())
    print(queue.first())
    queue.dequeue()
    print(queue.first())
    queue.remove()
    print(queue.len())
