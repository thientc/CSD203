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

    def preOrderTraversal(self, node=None):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        if node is None:
            node = self.root
        if node is not None:
            self._traversal_list.append(node.key)
            self.preOrderTraversal(node.lChild)
            self.preOrderTraversal(node.rChild)
        #-------------------------------------- 
        return self._traversal_list

    def inOrderTraversal(self, node=None):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        if node is None:
            node = self.root
        if node is not None:
            self.inOrderTraversal(node.lChild)
            self._traversal_list.append(node.key)
            self.inOrderTraversal(node.rChild)
        #-------------------------------------- 
        return self._traversal_list

    def postOrderTraversal(self, node=None):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        if node is None:
            node = self.root
        if node is not None:
            self.postOrderTraversal(node.lChild)
            self.postOrderTraversal(node.rChild)
            self._traversal_list.append(node.key)
        #-------------------------------------- 
        return self._traversal_list

    def search(self, key, node=None):
        """This method is used for searching key in the current tree
        """
        found = False
        #---------- your code here ------------
        if node is None:
            node = self.root
        if node is None:
            found = False
        if node.key == key:
            found = True
        elif key < node.key:
            return self.search(key, node.lChild)
        else:
            return self.search(key, node.rChild)
        #-------------------------------------- 
        return found
        
    def parentKey(self, key, node=None):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        #---------- your code here ------------
        if node is None:
            parent_key = None
        if node.key == key:
            parent_key = key
        elif key < node.key:
            return self.parentKey(node.lChild, key, node)
        else:
            return self.parentKey(node.rChild, key, node)

        #-------------------------------------- 
        return parent_key
    
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        #---------- your code here ------------
        def height(node):
            if node is None:
                return 0
            return max(height(node.lChild), height(node.rChild)) + 1
        height = self.get_height()
        #-------------------------------------- 
        return height(self.root)
    
    def count_leaves(self, node=None):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        #---------- your code here ------------
        if node is None:
            node = self.root
        if node is None:
            return 0
        if node.lChild is None and node.rChild is None:
            return 1
        return self.count_leaves(node.lChild) + self.count_leaves(node.rChild)
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