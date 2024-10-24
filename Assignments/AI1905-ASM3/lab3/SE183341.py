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

        # ---------- your code here ------------
        def preOrderTraversalHelper(node):
            if node is not None:
                self._traversal_list.append(node.key)
                preOrderTraversalHelper(node.lChild)
                preOrderTraversalHelper(node.rChild)

        preOrderTraversalHelper(self.root)
        # --------------------------------------
        return self._traversal_list

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []

        # ---------- your code here ------------
        def inOrderTraversalHelper(node):
            if node is not None:
                inOrderTraversalHelper(node.lChild)
                self._traversal_list.append(node.key)
                inOrderTraversalHelper(node.rChild)

        inOrderTraversalHelper(self.root)
        # --------------------------------------
        return self._traversal_list

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []

        # ---------- your code here ------------
        def postOrderTraversalHelper(node):
            if node is not None:
                postOrderTraversalHelper(node.lChild)
                postOrderTraversalHelper(node.rChild)
                self._traversal_list.append(node.key)

        postOrderTraversalHelper(self.root)
        # --------------------------------------
        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False

        # ---------- your code here ------------
        def searchNode(node, key):
            if node is None or node.key == key:
                return node
            if key < node.key:
                return searchNode(node.lChild, key)
            return searchNode(node.rChild, key)

        found = searchNode(self.root, key) is not None
        # --------------------------------------
        return found

    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0

        # ---------- your code here ------------
        def parentKeyHelper(node, key, parent):
            if node is None:
                return None
            if node.key == key:
                return parent
            if key < node.key:
                return parentKeyHelper(node.lChild, key, node)
            return parentKeyHelper(node.rChild, key, node)

        parent = parentKeyHelper(self.root, key, None)
        parent_key = parent.key if parent else None
        # --------------------------------------
        return parent_key

    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0

        # ---------- your code here ------------
        def getHeightHelper(node):
            if self.root is None:
                return -1
            stack = [(self.root, 0)]
            while stack:
                current, depth = stack.pop()
                height = max(height, depth)
                if current.lChild is not None:
                    stack.append((current.lChild, depth + 1))
                if current.rChild is not None:
                    stack.append((current.rChild, depth + 1))
        # --------------------------------------
        return height

    def count_leaves(self):
        """This method is used to count all leaves of the current tree
        """
        leaves = 0

        # ---------- your code here ------------
        def countLeavesHelper(node):
            if node is None:
                return 0
            if node.lChild is None and node.rChild is None:
                return 1
            return countLeavesHelper(node.lChild) + countLeavesHelper(node.rChild)

        leaves = countLeavesHelper(self.root)
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
