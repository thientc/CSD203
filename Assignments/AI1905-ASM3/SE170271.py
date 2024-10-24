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

    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self._preO(self.root)
        
        #-------------------------------------- 
        return self._traversal_list
    
    def _preO(self, node):
        if node:
            self._traversal_list.append(node.key)
            self._preO(node.lChild)
            self._preO(node.rChild)   
            
        
    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self._inO(self.root)
        
        
        #-------------------------------------- 
        return self._traversal_list
    def _inO(self, node):
        if node:
            self._inO(node.lChild)
            self._traversal_list.append(node.key)
            self._inO(node.rChild)
    
    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self._postOrder(self.root)
        #-------------------------------------- 
        return self._traversal_list
    def _postOrder(self, node):
        if node:
            self._postOrder(node.lChild)
            self._postOrder(node.rChild)
            self._traversal_list.append(node.key)

    
    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        #---------- your code here ------------
        self._search(self.root, key)
        #-------------------------------------- 
        return found

    def _search(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif node.key > key:
            return self._search(node.lChild, key)
        else:
            return self._search(node.rChild, key)
        
         
    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        #---------- your code here ------------
        return self._parentKey(self.root, key)
        #
        #
        #-------------------------------------- 
        return parent_key
        
        
    def _parentKey(self, node, key, parent=None):
        if node is None:
            return None
        if node.key == key:
            return parent.key if parent else None
        elif key < node.key:
            return self._parentKey(node.lChild, key, node)
        else:
            return self._parentKey(node.rChild, key, node)
    
    
        
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        #---------- your code here ------------
        return self._get_height(self.root)
        #
        #
        #-------------------------------------- 
        return height
        

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._get_height(node.lChild)
            right_height = self._get_height(node.rChild)
            return max(left_height, right_height) + 1
        
    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        #---------- your code here ------------
        return self._count_leaves(self.root)
        #
        #
        #-------------------------------------- 
        return leaves
        
        
        
    def _count_leaves(self, node):
        if node is None:
            return 0
        if node.lChild is None and node.rChild is None:
            return 1
        return self._count_leaves(node.lChild) + self._count_leaves(node.rChild)
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
    print("\nHeight of the tree:  ", t.get_height())
    print("\nAmount of leaf Nodes:  ", t.count_leaves())

    

















