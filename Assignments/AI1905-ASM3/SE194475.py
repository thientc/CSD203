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

    def preOrderHelper(self, node):
        if node:
            self._traversal_list.append(node.key)
            self.preOrderHelper(node.lChild)
            self.preOrderHelper(node.rChild)

    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        # ---------- your code here ------------
        self.preOrderHelper(self.root)

        # --------------------------------------
        return self._traversal_list

    def inOrderHelper(self, node):
        if node:
            self.inOrderHelper(node.lChild)
            self._traversal_list.append(node.key)
            self.inOrderHelper(node.rChild)

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        # ---------- your code here ------------
        self.inOrderHelper(self.root)
        # --------------------------------------
        return self._traversal_list

    def postOrderHelper(self, node):
        if node:
            self.postOrderHelper(node.lChild)
            self.postOrderHelper(node.rChild)
            self._traversal_list.append(node.key)

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        # ---------- your code here ------------
        self.postOrderHelper(self.root)
        # --------------------------------------
        return self._traversal_list

    def searchNode(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.searchNode(node.lChild, key)
        return self.searchNode(node.rChild, key)

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        # ---------- your code here ------------
        found = self.searchNode(self.root, key) is not None
        # --------------------------------------
        return found

    def parentHelper(self, node, key, parent=None):
        if node is None:
            return None
        if node.key == key:
            return parent
        elif key < node.key:
            return self.parentHelper(node.lChild, key, node)
        else:
            return self.parentHelper(node.rChild, key, node)

    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        # ---------- your code here ------------
        parent = self.parentHelper(self.root, key)
        parent_key = parent.key if parent else None
        # --------------------------------------
        return parent_key

    def heightHelper(self, node):
        if node is None:
            return 0
        return 1 + max(self.heightHelper(node.lChild), self.heightHelper(node.rChild))

    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        # ---------- your code here ------------
        height = self.heightHelper(self.root)
        # --------------------------------------
        return height

    def countLeavesHelper(self, node):
        if node is None:
            return 0
        if node.lChild is None and node.rChild is None:
            return 1
        return self.countLeavesHelper(node.lChild) + self.countLeavesHelper(node.rChild)

    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        # ---------- your code here ------------
        leaves = self.countLeavesHelper(self.root)
        # --------------------------------------
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