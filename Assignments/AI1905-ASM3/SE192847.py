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

    def preOrder(self, cur, seq: list):
        if cur is not None:
            seq.append(cur.key)
            self.preOrder(cur.lChild, seq)
            self.preOrder(cur.rChild, seq)

        return seq

    def inOrder(self, cur, seq: list):
        if cur is not None:
            self.inOrder(cur.lChild, seq)
            seq.append(cur.key)
            self.inOrder(cur.rChild, seq)

        return seq

    def postOrder(self, cur, seq: list):
        if cur is not None:
            self.postOrder(cur.lChild, seq)
            self.postOrder(cur.rChild, seq)
            seq.append(cur.key)

        return seq


    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------

        self._traversal_list = self.preOrder(self.root, [])

        #-------------------------------------- 
        return self._traversal_list

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------

        self._traversal_list = self.inOrder(self.root, [])

        #-------------------------------------- 
        return self._traversal_list

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------

        self._traversal_list = self.postOrder(self.root, [])

        #-------------------------------------- 
        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        #---------- your code here ------------

        self.preOrderTraversal()
        if key in self._traversal_list:
            found = True

        #-------------------------------------- 
        return found

    def findParentKey(self, node, key):
        if node is None:
            return None

        if node is not None:
            if key < node.key:
                return node.key if node.lChild and key == node.lChild.key else self.findParentKey(node.lChild, key)

            elif key > node.key:
                return node.key if node.rChild and key == node.rChild.key else self.findParentKey(node.rChild, key)

        return

    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        #---------- your code here ------------
        # if self.root is None:
        #     return None
        #
        # cur = self.root
        #
        # while cur:
        #     if key < cur.key:
        #         if cur.lChild and key == cur.lChild.key:
        #             parent_key = cur.key
        #             break
        #
        #         cur = cur.lChild
        #     elif key > cur.key:
        #         if cur.rChild and key == cur.rChild.key:
        #             parent_key = cur.key
        #             break
        #         cur = cur.rChild
        #     else:
        #         break

        parent_key = self.findParentKey(self.root, key)

        #-------------------------------------- 
        return parent_key

    def height(self, node):
        if node is None:
            return -1
        leftHeight = self.height(node.lChild)
        rightHeight = self.height(node.rChild)

        return 1 + max(leftHeight, rightHeight)

    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        #---------- your code here ------------

        height = self.height(self.root)

        #-------------------------------------- 
        return height

    def isLeaf(self, node):
        return node.lChild == None and node.rChild == None

    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        #---------- your code here ------------
        def leavesCount(node):
            if node is None:
                return 0

            if self.isLeaf(node):
                return 1

            return leavesCount(node.lChild) + leavesCount(node.rChild)

        leaves = leavesCount(self.root)

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


    k = 12
    if (t.search(k)):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")
        
    print("\nParent key of 20 :  ", t.parentKey(20))
    print("\nAmount of leaf Nodes:  ", t.count_leaves())
    print("\nHeight of the tree:  ", t.get_height())
