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

    def _preOrderTraversal(self, node):
        if node is not None: 
            self._traversal_list.append(node.key)
            self._preOrderTraversal(node.lChild)
            self._preOrderTraversal(node.rChild)

    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self._preOrderTraversal(self.root)
        #-------------------------------------- 
        return self._traversal_list

    def _inOrderTraversal(self, node):
        if node is not None: 
            self._inOrderTraversal(node.lChild)
            self._traversal_list.append(node.key)
            self._inOrderTraversal(node.rChild)

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self._inOrderTraversal(self.root)
        #-------------------------------------- 
        return self._traversal_list
    
    def _postOrderTraversal(self, node):
        if node is not None: 
            self._postOrderTraversal(node.lChild)
            self._postOrderTraversal(node.rChild)
            self._traversal_list.append(node.key)

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self._postOrderTraversal(self.root)
        #-------------------------------------- 
        return self._traversal_list

    def _search(self, node, key):
        if self.root is None:
            return None
        while node.rChild is not None and node.lChild is not None: 
            if key < node.key: node = node.lChild 
            if key > node.key: node = node.rChild
        if node.key == key: 
            return True
        else: 
            return False
        
    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        #---------- your code here ------------
        found = self._search(self.root, key)
        #-------------------------------------- 
        return found
        
    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        #---------- your code here ------------
        #
        pass
        #
        #
        #-------------------------------------- 
        return parent_key
    
    def _get_height(self, node):
        if node is None:
            return -1
        return 1 + max(self._get_height(node.lChild), self._get_height(node.rChild))
    
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        #---------- your code here ------------
        height = self._get_height(self.root)
        #-------------------------------------- 
        return height
    
    def is_leaf(self, node):
        return node.lChild is None and node.rChild is None
    
    def _count_leaves(self, node):
        if node is None:
            return 0
        if self.is_leaf(node):
            return 1
        return self._count_leaves(node.lChild) + self._count_leaves(node.rChild)

    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        #---------- your code here ------------
        leaves = self._count_leaves(self.root)
        #-------------------------------------- 
        return leaves
    
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