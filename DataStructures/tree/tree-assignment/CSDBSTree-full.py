class Node:
    def __init__(self, key):
        self.rChild = None
        self.lChild = None
        self.key = key


class BSTree:
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

    def findFather(self, k):
        if (self.root == None):
            return -9999
        if (self.root.key == None):
            return -9999
        return self.findFatherRec(self.root, k)

    def findFatherRec(self, tmp, k):
        if (tmp == None):
            return -9999
        if (tmp.lChild == None) and (k<tmp.key):
            return -9999
        if (tmp.rChild == None) and (k>tmp.key):
            return -9999
        if (tmp.lChild.key == k) or (tmp.rChild.key ==k):
            return tmp.key
        if (k < tmp.key):
            return self.findFatherRec(tmp.lChild, k)
        return self.findFatherRec(tmp.rChild, k)

    def calHeight(self):
        return self.calHeightRec(self.root)
    def calHeightRec(self, tmp):
        if (tmp == None):
            return 0
        if (tmp.lChild == None) and (tmp.rChild == None):
            return 0
        if self.calHeightRec(tmp.lChild) > self.calHeightRec(tmp.rChild):
            return 1 + self.calHeightRec(tmp.lChild)
        return 1 + self.calHeightRec(tmp.rChild)

    def countLeaf(self):
        return self.countLeafRec(self.root)
    def countLeafRec(self, tmp):
        if (tmp == None):
            return 0
        if (tmp.lChild == None) and (tmp.rChild == None):
            return 1
        return self.countLeafRec(tmp.lChild) + self.countLeafRec(tmp.rChild)


    def sum(self):
        return self.sumRec(self.root)
    def sumRec(self, tmp):
        if (tmp == None):
            return 0
        return self.sumRec(tmp.lChild) + tmp.key + self.sumRec(tmp.rChild)

    def countNode(self):
        return self.countNodeRec(self.root)

    def countNodeRec(self, tmp):
        if (tmp == None):
            return 0
        return self.countNodeRec(tmp.lChild) + 1 + self.countNodeRec(tmp.rChild)

    def delete(self, k):
        self.root = self.deleteRec(self.root, k)

    def deleteRec(self, tmp, k):
        # Base case
        if tmp is None:
            return tmp
        # Recursive calls for ancestors of node to be deleted
        if tmp.key > k:
            tmp.lChild = self.deleteRec(tmp.lChild, k)
            return tmp
        elif tmp.key < k:
            tmp.rChild = self.deleteRec(tmp.rChild, k)
            return tmp
        # We reach here when root is the node to be deleted.

        # If one of the children is empty
        if tmp.lChild is None:
            temp = tmp.rChild
            return temp
        elif tmp.rChild is None:
            temp = tmp.lChild
            return temp

        # If both children exist
        else:
            succParent = tmp
            succ = tmp.rChild
            while succ.left is not None:
                succParent = succ
                succ = succ.lChild
            if succParent != tmp:
                succParent.lChild = succ.lChild
            else:
                succParent.rChild = succ.rChild
            tmp.key = succ.key
            return tmp
    # ======================================================

def processing():
    t = BSTree()
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
    print("\nBFT: ")
    t.bftTree()
    print("\nAmount of Nodes:  ", t.countNode())
    k = 20
    if (t.search(k) == True):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")
    print("\nFather of Nodes 20 :  ", t.findFather(20))
    print("\nSum of Nodes:  ", t.sum())
    print("\nAmount of leaf Nodes:  ", t.countLeaf())
    print("\nHeight of the tree:  ", t.calHeight())

    print("\n\n\nTree after deleting node 20\n")
    print("\nInOrder: ")
    t.delete(20)
    print(t.inOrderTraversal())


if __name__ == '__main__':
    processing()