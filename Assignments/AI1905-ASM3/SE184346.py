class Node:
    def __init__(self, key):
        self.rChild = None
        self.lChild = None
        self.key = key


class CSDBSTree:
    """Template for CSDBSTree class
    """
    _slot_ = "root", "_traversal_list"

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
        def preOrder(node):
            if (node != None):
                self._traversal_list.append(node.key)
                preOrder(node.lChild)
                preOrder(node.rChild)
        preOrder(self.root)
        # --------------------------------------
        return self._traversal_list

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        # ---------- your code here ------------
        def inOrder(node):
            if (node != None):
                inOrder(node.lChild)
                self._traversal_list.append(node.key)
                inOrder(node.rChild)
        inOrder(self.root)
        # --------------------------------------
        return self._traversal_list

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        # ---------- your code here ------------
        def postOrder(node):
            if (node != None):
                postOrder(node.lChild)
                postOrder(node.rChild)
                self._traversal_list.append(node.key)
        postOrder(self.root)
        # --------------------------------------
        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        # ---------- your code here ------------
        def searchNode(node, key):
            if node is None:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return searchNode(node.lChild, key)
            else:
                return searchNode(node.rChild, key)
        found = searchNode(self.root, key)
        # --------------------------------------
        return found

    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        # ---------- your code here ------------
        def count(key):
            parent = None
            t = self.root
            while t is not None:
                if key == t.key:
                    break
                parent = t
                if key < t.key:
                    t = t.lChild
                else: t = t.rChild
            if t is None or t == self.root:
                return None
            return parent.key
        parent_key = count(key)
        # --------------------------------------
        return parent_key

    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        # ---------- your code here ------------
        def height(node):
            if node is None:
                return -1
            left_height = height(node.lChild)
            right_height = height(node.rChild)
            return max(left_height, right_height) +1
        height = height(self.root)
        # --------------------------------------
        return height

    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        # ---------- your code here ------------
        def count(node):
            if node is None:
                return 0
            if node.rChild is None and node.lChild is None:
                return 1
            return count(node.rChild) + count(node.lChild)
        leaves = count(self.root)
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