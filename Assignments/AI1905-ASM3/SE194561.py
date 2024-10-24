class Node:
    def __init__(self, key):
        self.rChild = None
        self.lChild = None
        self.key = key

class CSDBSTree:
    """Template for CSDBSTree class
    """
    __slots__ = "root", "_traversal_list"
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

    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self.preOrderMain(self.root)
        #
        #
        #-------------------------------------- 
        return self._traversal_list
    def preOrderMain(self,node):
        if (node != None):
            self._traversal_list.append(node.key)
            self.preOrderMain(node.lChild)
            self.preOrderMain(node.rChild)

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self.inOrderMain(self.root)
        #
        #
        #-------------------------------------- 
        return self._traversal_list
    def inOrderMain(self,node):
        if (node != None):
            self.inOrderMain(node.lChild)
            self._traversal_list.append(node.key)
            self.inOrderMain(node.rChild)

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self.postOrderMain(self.root)
        #
        #
        #-------------------------------------- 
        return self._traversal_list
    def postOrderMain(self,node):
        if (node != None):
            self.postOrderMain(node.lChild)
            self.postOrderMain(node.rChild)
            self._traversal_list.append(node.key)

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        #---------- your code here ------------
        #
        #
        #-------------------------------------- 
        return found
        
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
        #---------- your code here ------------
        #
        #
        #
        #-------------------------------------- 
        return height
    
    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        #---------- your code here ------------
        #
        #
        #
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