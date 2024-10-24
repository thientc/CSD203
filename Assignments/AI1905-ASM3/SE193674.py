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

    def _pre_order(self, node, lst_pre=None):
        if lst_pre is None:
            lst_pre = []
        if node is not None:
            lst_pre.append(node.key)
            self._pre_order(node.lChild, lst_pre)
            self._pre_order(node.rChild, lst_pre)
        return lst_pre
    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        return self._pre_order(self.root)

    def _in_order(self, node, lst_in=None):
        if lst_in is None:
            lst_in = []
        if node is not None:
            self._in_order(node.lChild, lst_in)
            lst_in.append(node.key)
            self._in_order(node.rChild, lst_in)
        return lst_in
    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        return self._in_order(self.root)

    def _post_order(self, node, lst_post=None):
        if lst_post is None:
            lst_post = []
        if node is not None:
            self._post_order(node.lChild, lst_post)
            self._post_order(node.rChild, lst_post)
            lst_post.append(node.key)
        return lst_post
    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        return self._post_order(self.root)

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        crr = self.root
        while crr is not None:
            if key == crr.key:
                found = True
                return True
            else:
                if key < crr.key:
                    crr = crr.lChild
                if key > crr.key:
                    crr = crr.rChild
        if not found:
            return False
        
    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        crr = self.root
        parent = None
        while crr is not None:
            if key < crr.key:
                parent = crr
                crr = crr.lChild
            elif key > crr.key:
                parent = crr
                crr = crr.rChild
            else:
                if parent:
                    return parent.key

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.lChild)
        right_height = self.height(node.rChild)
        return max(left_height, right_height) + 1
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        return self.height(self.root)
    
    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        lst = [self.root]
        while lst:
            node = lst.pop(0)
            if node.lChild is None and node.rChild is None:
                leaves += 1
            else:
                if node.lChild is not None:
                    lst.append(node.lChild)
                if node.rChild is not None:
                    lst.append(node.rChild)
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
    
    k = 15
    if (t.search(k)):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")

    print("\nParent key of 20 :  ", t.parentKey(20))
    print("\nAmount of leaf Nodes:  ", t.count_leaves())
    print("\nHeight of the tree:  ", t.get_height())