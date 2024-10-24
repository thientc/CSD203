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

    def preOrderTraversal(self,node):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        if node != None:
            self._traversal_list.append(node.key)
            self.preOrderTraversal(node.lChild)
            self.preOrderTraversal(node.rChild) 
         
        return self._traversal_list

    def inOrderTraversal(self,node):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        if node != None:
            self.inOrderTraversal(node.lChild)
            self._traversal_list.append(node.key)
            self.inOrderTraversal(node.rChild)
        
        return self._traversal_list

    def postOrderTraversal(self,node):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        if node != None:
            self.postOrderTraversal(node.lChild)
            self.postOrderTraversal(node.rChild)
            self._traversal_list.append(node.key)    
        
        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        
        return found
        
    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        child = Node(key)

        return parent_key
    
    def get_height(self,node):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        
        if node is None:
            return -1
        left_height = self.get_height(node.lChild)
        right_height = self.get_height(node.rChild)
        return max(left_height, right_height) 

    def is_leaf(self, node):
        if node.rChild is None and node.lChild is None:
            return True
        else:
            return False
    
    def count_leaves(self,node):
        """This method is used to all leaves of the current tree
        """
        if node is None:
            return 0
        if self.is_leaf(node):
            return 1
        return self.count_leaves(node.lChild) + self.count_leaves(node.rChild)

    
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
    print(t.preOrderTraversal(t.root))
    print("\nInOrder: ")
    print(t.inOrderTraversal(t.root))
    print("\nPostOrder: ")
    print(t.postOrderTraversal(t.root))
    
    k = 20
    if (t.search(k)):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")
        
    print("\nParent key of 20 :  ", t.parentKey(20))
    print("\nAmount of leaf Nodes:  ", t.count_leaves(t.root))
    print("\nHeight of the tree:  ", t.get_height(t.root))
