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

    def preOrderTraversalNode(self,node):
        if node:
            self._traversal_list.append(node.key)
            self.preOrderTraversalNode(node.lChild)
            self.preOrderTraversalNode(node.rChild)

    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """

        self._traversal_list = []
        self.preOrderTraversalNode(self.root)
        return self._traversal_list

    def inOrderTraversalNode(self,node):
        if node:
            self.inOrderTraversalNode(node.lChild)
            self._traversal_list.append(node.key)
            self.inOrderTraversalNode(node.rChild)
    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """

        self._traversal_list = []
        self.inOrderTraversalNode(self.root)
        return self._traversal_list
    def postOderTraversalNode(self,node):
        if node:
            self.postOderTraversalNode(node.lChild)
            self.postOderTraversalNode(node.rChild)
            self._traversal_list.append(node.key)

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        self.postOderTraversalNode(self.root)
        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        current = self.root
        while current:
            if key == current.key:
                found = True
                break
            elif key < current.key:
                current = current.lChild
            elif key > current.key:
                current = current.rChild
        return found

    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0

        return parent_key


    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        current = self.root
        height= max(self.get_height(current.rChild),self.get_height(current.lChild))+1
        return height
    def test_count_leaves(self,node):
        pass

    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0

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