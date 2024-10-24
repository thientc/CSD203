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
    def preOrder(self, node):
        if node:
            self._traversal_list.append(node.key)
            self.preOrder(node.lChild)
            self.preOrder(node.rChild)
    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self.preOrder(self.root)
        #-------------------------------------- 
        return self._traversal_list
    def inOrder(self, node):
        if node:
            self.inOrder(node.lChild)
            self._traversal_list.append(node.key)
            self.inOrder(node.rChild)
    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self.inOrder(self.root)
        #-------------------------------------- 
        return self._traversal_list
    def postOrder(self, node):
        if node:
            self.postOrder(node.lChild)
            self.postOrder(node.rChild)
            self._traversal_list.append(node.key)
    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self.postOrder(self.root)
        #-------------------------------------- 
        return self._traversal_list
    def searching(self, node, key):
        if node is None or node.key == key: return node
        if key < node.key: return self.searching(node.lChild, key)
        return self.searching(node.rChild, key)
    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        #---------- your code here ------------
        found = self.searching(self.root, key)
        #-------------------------------------- 
        return found
    def parent(self, node, key, parent):
        if node is None:
            return None
        if node.key == key:
            return parent.key if parent else None
        elif key < node.key:
            return self.parent(node.lChild, key, node)
        else:
            return self.parent(node.rChild, key, node)
    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        #---------- your code here ------------
        parent_key = self.parent(self.root, key, None)
        #-------------------------------------- 
        return parent_key
    def height(self, node):
        if node is None: return -1
        else:
            left_height = self.height(node.lChild)
            right_height = self.height(node.rChild)
            return 1 + max(left_height, right_height)
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        #---------- your code here ------------
        height = int(self.height(self.root))
        #-------------------------------------- 
        return height
    def count(self, node):
        if node is None:
            return 0
        if node.lChild is None and node.rChild is None:
            return 1
        return self.count(node.lChild) + self.count(node.rChild)
    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        #---------- your code here ------------
        leaves = self.count(self.root)
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
    
    k = 3
    if (t.search(k)):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")
        
    print("\nParent key of k :  ", t.parentKey(k))
    print("\nAmount of leaf Nodes:  ", t.count_leaves())
    print("\nHeight of the tree:  ", t.get_height())