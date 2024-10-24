class Node:
    def __init__(self, key):
        self.rChild = None
        self.lChild = None
        self.key = key

class CSDBSTree:
    """Template for CSDBSTree class
    """
    __slot__ = "root", "_traversal_list"
    def __init__(self):
        self.root = None
        self._traversal_list = []

    def insertNode(self, node, key):
        if (node == None):
            node = Node(key)
        elif (key < node.key):
            node.lChild = self.insertNode(node.lChild, key)
        elif (key > node.key):
            node.rChild = self.insertNode(node.rChild, key)
        return node

    def insert(self, key):
        """This method is used to insert a key into the current tree.
        """

        self.root = self.insertNode(self.root, key)

    def is_leaf(self, node):
        return node.rChild is None and node.lChild is None

    def preOrder(self, nkey):
        if nkey is not None:
            self._traversal_list.append(nkey.key)
            self.preOrder(nkey.lChild)
            self.preOrder(nkey.rChild)

    def postOrder(self, nkey):
        if nkey is not None:
            self.postOrder(nkey.lChild)
            self.postOrder(nkey.rChild)
            self._traversal_list.append(nkey.key)

    def inOrder(self, nkey):
        if nkey is not None:
            self.inOrder(nkey.lChild)
            self._traversal_list.append(nkey.key)
            self.inOrder(nkey.rChild)

    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        self.preOrder(self.root)
        return self._traversal_list

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        self.inOrder(self.root)
        return self._traversal_list

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        self.preOrder(self.root)
        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        found = self.SearchNode(key)
        return found

    def SearchNode(node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return SearchNode(node.lChild, key)
        else:
            return SearchNode(node.rChild, key)
        
    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        #---------- your code here ------------
        #
        #
        #
        #-------------------------------------- 
        return parent_key


    
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        if not self.root:
            return -1
        queue = [(self.root, 0)]
        while queue:
            node, height01 = queue.pop(0)
            height = max(height, height01)
            if node.lChild:
                queue.append((node.lChild, height01 + 1))
            if node.rChild:
                queue.append((node.rChild, height01 + 1))
        return height
    
    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        leaves = self.count(self.root)
        return leaves

    def count(self, nkey):
        if nkey is None:
            return 0
        if self.is_leaf(nkey):
            return 1
        left_count = self.count(nkey.lChild)
        right_count = self.count(nkey.rChild)
        return (left_count + right_count)

    # ======================================================

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
    t.insert(27)
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
    print("\nAmount of leaf Nodes:  ", t.count_leaves())
    print("\nHeight of the tree:  ", t.get_height())


