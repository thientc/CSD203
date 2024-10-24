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
        self._traversal_list = []

        # ---------- your code here ------------
        def _pre_order(node):
            if node:
                self._traversal_list.append(node.key)
                _pre_order(node.lChild)
                _pre_order(node.rChild)

        _pre_order(self.root)
        # --------------------------------------
        return self._traversal_list

    def inOrderTraversal(self):
        self._traversal_list = []

        # ---------- your code here ------------
        def _in_order(node):
            if node:
                _in_order(node.lChild)
                self._traversal_list.append(node.key)
                _in_order(node.rChild)

        _in_order(self.root)
        # --------------------------------------
        return self._traversal_list

    def postOrderTraversal(self):
        self._traversal_list = []

        # ---------- your code here ------------
        def _post_order(node):
            if node:
                _post_order(node.lChild)
                _post_order(node.rChild)
                self._traversal_list.append(node.key)

        _post_order(self.root)

        # --------------------------------------
        return self._traversal_list

    def search(self, key):
        found = False

        # ---------- your code here ------------
        def find(node, key):
            if node is None:
                return False
            elif node.key == key:
                return True
            elif key < node.key:
                return find(node.lChild, key)
            else:
                return find(node.rChild, key)

        found = find(self.root, key)
        # --------------------------------------
        return found

    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0

        # ---------- your code here ------------
        def find_parent(node, key):
            if node is None or node.key == key:
                return None
            elif ((node.lChild and node.lChild.key == key) or
                  (node.rChild and node.rChild.key == key)):
                return node.key
            elif key < node.key:
                return find_parent(node.lChild, key)
            else:
                return find_parent(node.rChild, key)

        parent_key = find_parent(self.root, key)
        # --------------------------------------
        return parent_key

    def get_height(self):
        # ---------- your code here ------------
        def height_check(node):
            if node is None:
                return -1
            return max(height_check(node.lChild), height_check(node.rChild)) + 1

        height = height_check(self.root)
        # --------------------------------------
        return height

    def count_leaves(self):
        # ---------- your code here ------------
        def count(node):
            if node is None:
                return 0
            if node is not None:
                if node.lChild is None and node.rChild is None:
                    return 1
            return count(node.lChild) + count(node.rChild)

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

    k = 25
    if (t.search(k)):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")

    print("\nParent key of 20 :  ", t.parentKey(20))
    print("\nAmount of leaf Nodes:  ", t.count_leaves())
    print("\nHeight of the tree:  ", t.get_height())
