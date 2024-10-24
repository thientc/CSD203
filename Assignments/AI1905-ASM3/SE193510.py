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
        if self.root is None:
            return -1

        def _preOrder(node):
            if node:
                self._traversal_list.append(node.key)
                _preOrder(node.lChild)
                _preOrder(node.rChild)

        _preOrder(self.root)
        #--------------------------------------
        return self._traversal_list

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        if self.root is None:
            return -1

        def _inOrder(node):
            if node:
                _inOrder(node.lChild)
                self._traversal_list.append(node.key)
                _inOrder(node.rChild)

        _inOrder(self.root)
        #-------------------------------------- 
        return self._traversal_list

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        if self.root is None:
            return -1

        def _postOrder(node):
            if node:
                _postOrder(node.lChild)
                _postOrder(node.rChild)
                self._traversal_list.append(node.key)

        _postOrder(self.root)
        #-------------------------------------- 
        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        #---------- your code here ------------
        def check_node(node, key):
            if node is None:
                return False
            if node.key == key:
                return True
            if key < node.key:
                return check_node(node.lChild, key)
            return check_node(node.rChild, key)

        found = check_node(self.root, key)

        #-------------------------------------- 
        return found
        
    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        #---------- your code here ------------
        def find_parent(node, key, parent):
            if node is None:
                return None
            if node.key == key:
                return parent
            if key < node.key:
                return find_parent(node.lChild, key, node)
            return find_parent(node.rChild, key, node)

        parent_node = find_parent(self.root, key, None)
        if parent_node:
            parent_key = parent_node.key
        #-------------------------------------- 
        return parent_key
    
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        #---------- your code here ------------
        def _get_height(node):
            if node is None:
                return 0
            left_height = _get_height(node.lChild)
            right_height = _get_height(node.rChild)
            return max(left_height, right_height) + 1
        if self.root is not None:
            height = _get_height(self.root) - 1
        else:
            height = 0
        #--------------------------------------
        return height

    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        #---------- your code here ------------
        def _count_leaves(node):
            if node is None:
                return 0
            if node.lChild is None and node.rChild is None:
                return 1
            return _count_leaves(node.lChild) + _count_leaves(node.rChild)

        leaves = _count_leaves(self.root)
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
    
    k = 30
    if (t.search(k)):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")
        
    print("\nParent key of 20 :  ", t.parentKey(20))
    print("\nAmount of leaf Nodes:  ", t.count_leaves())
    print("\nHeight of the tree:  ", t.get_height())