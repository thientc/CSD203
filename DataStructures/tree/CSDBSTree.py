class CSDNode:
    def __init__(self, key):
        self.rChild = None
        self.lChild = None
        self.key = key

class CSDBSTree:
    def __init__(self):
        self.root = None
        self._leaves_count = 0

    def num_children(self, node):
        pass
    
    def is_leaf(self, node):
        if node.lChild is None and node.rChild is None:
            return True
        return False 
    
    def insertKey(self, tmp, new_key):
        if (tmp == None):
            tmp = CSDNode(new_key)
        elif (new_key < tmp.key):
            tmp.lChild = self.insertKey(tmp.lChild, new_key)
        elif (new_key > tmp.key):
            tmp.rChild = self.insertKey(tmp.rChild, new_key)
        return tmp

    def insert(self, new_key):
        self.root = self.insertKey(self.root, new_key)

    def preOrder(self, tmp):
        if (tmp != None):
            print(tmp.key)
            self.preOrder(tmp.lChild)
            self.preOrder(tmp.rChild)
            
    def postOrder(self, tmp):
        if (tmp != None):
            self.postOrder(tmp.lChild)
            self.postOrder(tmp.rChild)
            print(tmp.key)
                
    def inOrder(self, tmp):
        if (tmp != None):
            self.inOrder(tmp.lChild)
            print(tmp.key)
            self.inOrder(tmp.rChild)

    def printTree1(self):
        self.preOrder(self.root)

    def printTree2(self):
        self.inOrder(self.root)

    def printTree3(self):
        self.postOrder(self.root)

    def count_leaves(self, node):
        if self.is_leaf(node):
            self._leaves_count += 1
        else:
            if node.lChild:
                self.count_leaves(node.lChild)
            if node.rChild:
                self.count_leaves(node.rChild)
        
    def leaf_node_count(self):
        self._leaves_count = 0
        self.count_leaves(self.root)
        return self._leaves_count

    def get_height(self):
        pass
    
    def min_value(self):
        pass
    
    def max_value(self):
        pass

    def delete_max(self):
        pass

    def delete_min(self):
        pass
    
    def average_leaves(self):
        pass
    

if __name__ == "__main__":
    t = CSDBSTree()
    data = [20, 10, 40, 15, 30, 7, 50, 17, 34, 26, 29, 3, 8, 12, 49]
    # data = [20, 10, 40]
    for item in data:
        t.insert(item)
        
    print(t.leaf_node_count())