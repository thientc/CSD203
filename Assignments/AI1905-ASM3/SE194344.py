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
        self.pre_order(self.root)
        return self._traversal_list

    def pre_order(self, node):
        if node:
            self._traversal_list.append(node.key)
            self.pre_order(node.lChild)
            self.pre_order(node.rChild)

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        self.in_order(self.root)

        return self._traversal_list

    def in_order(self, node):
        if node:
            self.in_order(node.lChild)
            self._traversal_list.append(node.key)
            self.in_order(node.rChild)
    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list_1 = self.inOrderTraversal()
        self._traversal_list = self._traversal_list_1[::-1]
        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False

        found = self.find(self.root, key)
        return found

    def find(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self.find(node.lChild, key)
        else:
            return self.find(node.rChild, key)

    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        result = self.parent_find(self.root, key, None)
        return result if result is not None else 0

    def parent_find(self, node, key, parent):
        if node is None:
            return None
        if node.key == key:
            return parent
        elif key < node.key:
            return self.parent_find(node.lChild, key, node.key)
        else:
            return self.parent_find(node.rChild, key, node.key)
    
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        height = self.take_height(self.root)
        if not self.root:
            height = -1
        return height

    def take_height(self, node: Node):
        if node is None:
            return 0
        return 1 + (max(self.take_height(node.rChild), self.take_height(node.lChild)))


    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        def _countLeaves(node):
            if node is None:
                return 0
            if node.lChild is None and node.rChild is None:
                return 1
            return _countLeaves(node.lChild) + _countLeaves(node.rChild)
        leaves = _countLeaves(self.root)
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
    t.preOrderTraversal()
    
    k = 20
    if (t.search(k)):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")
        
    print("\nParent key of 20 :  ", t.parentKey(20))
    print("\nAmount of leaf Nodes:  ", t.count_leaves())
    print("\nHeight of the tree:  ", t.get_height())