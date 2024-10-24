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

    def _pre_order_helper(self, node):

        if node:
            self._traversal_list.append(node.key)
            self._pre_order_helper(node.lChild)
            self._pre_order_helper(node.rChild)
    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        self._pre_order_helper(self.root)
        return self._traversal_list

    def _in_order_helper(self, node):
        if node:
            self._in_order_helper(node.lChild)
            self._traversal_list.append(node.key)
            self._in_order_helper(node.rChild)
    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        self._in_order_helper(self.root)
        return self._traversal_list

    def _post_order_helper(self, node):
        if node:
            self._post_order_helper(node.lChild)
            self._post_order_helper(node.rChild)
            self._traversal_list.append(node.key)
    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        self._post_order_helper(self.root)

        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        current = self.root
        while current is not None:
            if current.key == key:
                found = True
                break
            elif key < current.key:
                current = current.lChild
            else:
                current = current.rChild
        return found
        
    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        current = self.root
        parent = None  

        while current is not None:
            if current.key == key:
                break
            parent = current
            if key < current.key:
                current = current.lChild  
            else:
                current = current.rChild  
        if current is None:  
            return None
        if parent is not None:
            parent_key = parent.key
            return parent_key

    def _get_height(self, node):
        height = 0
        if node is None:
            return height
        else:
            left_height = self._get_height(node.lChild)
            right_height = self._get_height(node.rChild)
            height = max(left_height, right_height) + 1
            return height
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = self._get_height(self.root)
        return height

    def _count_leaves_helper(self, node):
        """Helper method to count leaf nodes in a subtree."""
        if node is None:
            return 0
        if node.lChild is None and node.rChild is None:
            return 1

        return self._count_leaves_helper(node.lChild) + self._count_leaves_helper(node.rChild)
    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = self._count_leaves_helper(self.root)
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
    t.insert(13)
    t.insert(5)
    t.insert(20)
    t.insert(30)
    t.insert(3)


    print(t.get_height())