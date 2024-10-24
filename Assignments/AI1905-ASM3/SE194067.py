
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
        """This method is used to insert a key into the current tree."""
        self.root = self.insertNode(self.root, key)

    def preOrderTraversal(self):
        """This is preorder traversal method."""
        self._traversal_list = []

        def preOrder(node):
            if node:
                self._traversal_list.append(node.key)
                preOrder(node.lChild)
                preOrder(node.rChild)

        preOrder(self.root)
        return self._traversal_list

    def inOrderTraversal(self):
        """This is inorder traversal method."""
        self._traversal_list = []

        def inOrder(node):
            if node:
                inOrder(node.lChild)
                self._traversal_list.append(node.key)
                inOrder(node.rChild)

        inOrder(self.root)
        return self._traversal_list

    def postOrderTraversal(self):
        """This is postorder traversal method."""
        self._traversal_list = []

        def postOrder(node):
            if node:
                postOrder(node.lChild)
                postOrder(node.rChild)
                self._traversal_list.append(node.key)

        postOrder(self.root)
        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree"""
        found = False

        def searchNode(node, key):
            if node is None:
                return False
            if node.key == key:
                return True
            elif key < node.key:
                return searchNode(node.lChild, key)
            else:
                return searchNode(node.rChild, key)

        return searchNode(self.root, key)

    def parentKey(self, key):
        """This method is used to find key of parent node if it exists"""
        parent_key = 0

        def findParent(node, parent, key):
            if node is None:
                return None
            if node.key == key:
                return parent
            elif key < node.key:
                return findParent(node.lChild, node, key)
            else:
                return findParent(node.rChild, node, key)

        parent = findParent(self.root, None, key)
        return parent.key if parent else None

    def get_height(self):
        """This method is used to get the height of the current tree"""
        height = 0

        def height(node):
            if node is None:
                return -1
            return 1 + max(height(node.lChild), height(node.rChild))

        return height(self.root)

    def count_leaves(self):
        """This method is used to count all leaves of the current tree"""
        leaves = 0

        def leaves(node):
            if node is None:
                return 0
            if node.lChild is None and node.rChild is None:
                return 1
            return leaves(node.lChild) + leaves(node.rChild)

        return leaves(self.root)

    def is_leave(self, node):
        """This method checks if a node is a leaf"""
        return node is not None and node.lChild is None and node.rChild is None


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

