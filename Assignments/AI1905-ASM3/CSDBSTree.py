class Node:
    def __init__(self, key):
        self.rChild = None
        self.lChild = None
        self.key = key


class CSDBSTree:
    __slot__ = "root", "_traversal_list"
    def __init__(self):
        self.root = None
        self._traversal_list = []

    def insertNode(self, tmp, key):
        if (tmp == None):
            tmp = Node(key)
        elif (key < tmp.key):
            tmp.lChild = self.insertNode(tmp.lChild, key)
        elif (key > tmp.key):
            tmp.rChild = self.insertNode(tmp.rChild, key)
        return tmp

    def insert(self, key):
        self.root = self.insertNode(self.root, key)

    def preOrderVisit(self, node):
        if (node != None):
            self._traversal_list.append(node.key)
            self.preOrderVisit(node.lChild)
            self.preOrderVisit(node.rChild)

    def preOrderTraversal(self):
        self._traversal_list = []
        self.preOrderVisit(self.root)
        return self._traversal_list

    def inOrderVisit(self, node):
        if (node != None):
            self.inOrderVisit(node.lChild)
            self._traversal_list.append(node.key)
            self.inOrderVisit(node.rChild)

    def inOrderTraversal(self):
        self._traversal_list = []
        self.inOrderVisit(self.root)
        return self._traversal_list

    def postOrder(self, node):
        if (node != None):
            self.postOrder(node.lChild)
            self.postOrder(node.rChild)
            self._traversal_list.append(node.key)

    def postOrderTraversal(self):
        self._traversal_list = []
        self.postOrder(self.root)
        return self._traversal_list

    def bftNode(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.key, end="   ")
        elif level > 1:
            self.bftNode(node.lChild, level - 1)
            self.bftNode(node.rChild, level - 1)

    def bftTree(self):
        h = self.calHeight()
        for i in range(1, h + 1):
            self.bftNode(self.root, i)

    def search(self, k):
        return self.searchRec(self.root, k)

    def searchRec(self, tmp, k):
        if (tmp == None):
            return False
        else:
            if (tmp.key == k):
                return True
            elif (tmp.key > k):
                return self.searchRec(tmp.lChild, k)
            else:
                return self.searchRec(tmp.rChild, k)

    def parentKey(self, k):
        if (self.root == None):
            return None
        if (self.root.key == None):
            return None
        return self.findFatherRec(self.root, k)

    def findFatherRec(self, node, k):
        if (node == None):
            return None
        if (node.lChild == None) and (k<node.key):
            return None
        if (node.rChild == None) and (k>node.key):
            return None
        if (node.lChild.key == k) or (node.rChild.key ==k):
            return node.key
        if (k < node.key):
            return self.findFatherRec(node.lChild, k)
        return self.findFatherRec(node.rChild, k)

    def get_height(self):
        return self.calHeightRec(self.root)
    
    def calHeightRec(self, tmp):
        if (tmp == None):
            return 0
        if (tmp.lChild == None) and (tmp.rChild == None):
            return 0
        if self.calHeightRec(tmp.lChild) > self.calHeightRec(tmp.rChild):
            return 1 + self.calHeightRec(tmp.lChild)
        return 1 + self.calHeightRec(tmp.rChild)

    def count_leaves(self):
        return self.countLeafRec(self.root)
    def countLeafRec(self, node):
        if (node == None):
            return 0
        if (node.lChild == None) and (node.rChild == None):
            return 1
        return self.countLeafRec(node.lChild) + self.countLeafRec(node.rChild)

if __name__ == '__main__':
    t = CSDBSTree()
    t.insert(15)
    t.insert(8)
    t.insert(25)
    t.insert(13)
    t.insert(5)
    t.insert(20)
    t.insert(30)
    t.insert(3)
    print("\nPreOrder: ")
    print(t.preOrderTraversal())
    print("\nInOrder: ")
    print(t.inOrderTraversal())
    print("\nPostOrder: ")
    print(t.postOrderTraversal())
    
    k = 20
    if (t.search(k)):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")
        
    print("\nParent key of 20 :  ", t.parentKey(20))
    print("\nHeight of the tree:  ", t.get_height())
    print("\nAmount of leaf Nodes:  ", t.count_leaves())

    


