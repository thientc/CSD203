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
        self.size = 0

    def is_empty(self):
        return self.size == 0

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

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p  # visit p before its subtrees
        for c in self.children(p):  # for each child c
            for other in self._subtree_preorder(c):  # do preorder of c's subtree
                yield other
    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        lst=self._traversal_list = []
        current = self.root
        def preOrderNode(node):
            if (node != None):
                lst.append(node.key)
                preOrderNode(node.lChild)
                preOrderNode(node.rChild)
        preOrderNode(current)
        return self._traversal_list

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        lst=self._traversal_list = []
        current = self.root
        def inOrderNode(node):
            if (node != None):
                inOrderNode(node.lChild)
                lst.append(node.key)
                inOrderNode(node.rChild)
        inOrderNode(current)
        return self._traversal_list

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        lst=self._traversal_list = []
        current = self.root
        def postOrderNode(node):
            if (node != None):
                postOrderNode(node.lChild)
                postOrderNode(node.rChild)
                lst.append(node.key)
        postOrderNode(current)
        return self._traversal_list
    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        lst = []
        current = self.root
        if self.root is None:
            return found
        else:
            def check(node):
                if (node != None):
                    check(node.lChild)
                    check(node.rChild)
                    lst.append(node.key)
            check(current)
        if key in lst:
            found =True
        return found

    def parentKey_recur(self,node):
            if node is None:
                return False
            self.parentKey(node.lChild)
            self.parentKey(node.rChild)
            return node
    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        #---------- your code here ------------
        tmp = self.root

        if tmp.lChild.key == key:
            parent_key = tmp.key
        elif tmp.rChild.key == key:
            parent_key = tmp.key


        #-------------------------------------- 
        return parent_key
    def get_height_recur(self,node):
        if node is None:
            return 0
        left_node_check = self.get_height_recur(node.lChild)
        right_node_check = self.get_height_recur(node.rChild)
        return  1 + max(left_node_check, right_node_check)
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        #---------- your code here ------------
        height = self.get_height_recur(self.root)
        #-------------------------------------- 
        return height
    def count_leaf(self, node):
        if node is None:
            return 0
        if node.lChild is None and node.rChild is None:
            return 1
        return (self.count_leaf(node.rChild))+(self.count_leaf(node.lChild))
    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = self.count_leaf(self.root)
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
    #
    k = 20
    if (t.search(k)):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")

    print("\nParent key of 20 :  ", t.parentKey(20))
    print("\nAmount of leaf Nodes:  ", t.count_leaves())
    print("\nHeight of the tree:  ", t.get_height())
