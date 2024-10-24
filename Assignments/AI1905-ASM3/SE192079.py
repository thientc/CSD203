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

    def preOrderTraversal(self, root):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        if root:
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)
        return self._traversal_list

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []

        return self._traversal_list

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []

        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        current = self.root
        while current:
            if current.key == key:
                return True
            else:
                if key < current.key:
                    current = current.lChild
                else:
                    current = current.rChild
        return found
        
    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """

        parent = None
        current = self.root
        while current:
            if current.key == key:
                return parent.key if parent else 0
            parent = current
            if key < current.key:
                current = current.lChild
            else:
                current = current.rChild
        return 0

    
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        def calculate_height(node):
            if not node:
                return -1
            left_height = calculate_height(node.lChild)
            right_height = calculate_height(node.rChild)
            return max(left_height, right_height) + 1

        return calculate_height(self.root)
    
    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        def count_leaves_helper(node):
            if not node:
                return 0
            if not node.lChild and not node.rChild:
                return 1  # Leaf node found
            return count_leaves_helper(node.lChild) + count_leaves_helper(node.rChild)

        return count_leaves_helper(self.root)

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
    # print("\nPreOrder: ")
    # print(t.preOrderTraversal())
    # print("\nInOrder: ")
    # print(t.inOrderTraversal())
    # print("\nPostOrder: ")
    # print(t.postOrderTraversal())
    #


    print(t.parentKey(5))
    print(t.get_height())
    print(t.count_leaves())