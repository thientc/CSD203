
class Node:
    def __init__(self, value):
      self.value = value
      self.next = None
class Linkedlist:
    def __init__(self):
      self.head = None
    def addToHead(self, x):
      node_new = Node(x)
      node_new.next = self.head
      self.head = node_new
    def addToTail(self, x):
      node_new = Node(x)
      if not self.head:
        self.head = node_new
        return
      current = self.head
      while current.next:
        current = current.next
      current.next = node_new
    def addAfter(self, p , x):
      current = self.head
      while current:
        if current.value == p:
          node_new = Node(x)
          node_new.next = current.next
          current.next = node_new
          return
        current = current.next

    def Traverse(self):
      current = self.head
      while current:
        print(current.value, end=" ")
        current = current.next
      print("None")

    def deleteFromHead(self):
      if not self.head:
        return None
      GiaTriCanXoa = self.head.value
      self.head = self.head.next
      return GiaTriCanXoa

    def deteleFromTail(self):
      if not self.head:
        return None
      if not self.head.next:
        removeValue = self.head.value
        self.head = None
        return removeValue
      current = self.head
      while current.next and current.next.next:
        current = current.next
      remove_Value = current.next.value
      current.next = None
      return remove_Value

    def deleteAfter(self, p):
      current = self.head
      while current:
        if current.value == p and current.next:
          removed_value = current.next.value
          current.next = current.next.next
          return removed_value
        current = current.next

    def deleteValue(self, x):
      if not self.head:
        return
      if self.head.value == x:
        self.head = self.head.next
        return
      current = self.head
      while current.next:
        if current.next.value == x:
          current.next = current.next.next
          return
        current = current.next

    def max(self):
        if not self.head:
          return None
        max_value = self.head.value
        current = self.head
        while current:
          if current.value > max_value:
            max_value = current.value
          current = current.next
        return max_value

    def min(self):
      if not self.head:
        return None
      min_value = self.head.value
      current = self.head
      while current:
        if current.value < min_value:
          min_value = current.value
        current = current.next
      return min_value

    def sum(self):
      total = 0
      current = self.head
      while current:
        total += current.value
        current = current.next
      return total

    def count(self):
      count = 0
      current = self.head
      while current:
        count += 1
        current = current.next
      return count

    def avg(self):
      count = self.count()
      return self.sum() / count if count > 0 else 0

    def is_sorted(self):
      if not self.head:
        return True
      current = self.head
      while current.next:
        if current.value > current.next.value:
          return False
        current = current.next
      return True

    def insert(self, x):
      new_node = Node(x)
      if not self.head or self.head.value >= x:
        new_node.next = self.head
        self.head = new_node
        return
      current = self.head
      while current.next and current.next.value < x:
        current = current.next
      new_node.next = current.next
      current.next = new_node

    def reverse(self):
      prev = None
      current = self.head
      while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
      self.head = prev


if __name__ == '__main__':
  gg = Linkedlist()
  gg.addToHead(10)
  gg.addToTail(20)
  gg.addAfter(20, 30)
  gg.deleteFromHead()
  gg.deteleFromTail()
  gg.deleteValue(20)
  gg.addToHead(10)
  gg.addToTail(20)
  gg.addToTail(30)
  gg.insert(40)
  print("Max:", gg.max())
  print("Min:", gg.min())
  print("Sum:", gg.sum())
  print("Avg:", gg.avg())
  gg.Traverse()

