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

    def pre_order_with_list(self, cur):
        lst = []
        if cur is not None:
            lst.append(cur.key)
            lst.extend(self.pre_order_with_list(cur.lChild))
            lst.extend(self.pre_order_with_list(cur.rChild))
        return lst

    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        # ---------- your code here ------------
        for i in self.pre_order_with_list(self.root):
            self._traversal_list.append(i)
        # --------------------------------------
        return self._traversal_list

    def inOrder_with_list(self, cur, lst: list):
        if cur is not None:
            self.inOrder_with_list(cur.lChild, lst)
            lst.append(cur.key)
            self.inOrder_with_list(cur.rChild, lst)

    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        self.inOrder_with_list(self.root, self._traversal_list)
        return self._traversal_list

    def postOrder_with_list(self, tmp, lst: list):
        if tmp is not None:
            self.postOrder_with_list(tmp.lChild, lst)
            self.postOrder_with_list(tmp.rChild, lst)
            lst.append(tmp.key)
        return lst

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        # ---------- your code here ------------
        self._traversal_list = self.postOrder_with_list(self.root, [])
        # --------------------------------------
        return self._traversal_list

    def search_recursive(self, root, k):
        if root is None:
            return None
        if root.key == k:
            return root
        elif k < root.key:
            return self.search_recursive(root.lChild, k)
        else:
            return self.search_recursive(root.rChild, k)

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        # ---------- your code here ------------
        result = self.search_recursive(self.root, key)
        if result is None:
            found = False
        else:
            found = True
        # --------------------------------------
        return found

    def parentKey(self, key):
        """This method is used to find key of parent node if it exists."""
        parent_key = 0
        if self.root is None:
            return None

        curr = self.root

        while curr:
            if key < curr.key:
                if curr.lChild and key == curr.lChild.key:
                    parent_key = curr.key
                    break
                curr = curr.lChild
            elif key > curr.key:
                if curr.rChild and key == curr.rChild.key:
                    parent_key = curr.key
                    break
                curr = curr.rChild
            else:
                break
        # --------------------------------------
        return parent_key

    def get_height_recursive(self, curr):
        if curr is None:
            return -1
        left_height = self.get_height_recursive(curr.lChild)
        right_height = self.get_height_recursive(curr.rChild)

        return max(left_height, right_height) + 1

    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        # ---------- your code here ------------
        height = self.get_height_recursive(self.root)
        # --------------------------------------
        return height

    def is_leaf(self, node):
        return node.lChild is None and node.rChild is None

    def collect_leaf_nodes(self, node, lst):
        if node is not None:
            if self.is_leaf(node):
                lst.append(node)  # Add leaf node to the list
            else:
                self.collect_leaf_nodes(node.lChild, lst)
                self.collect_leaf_nodes(node.rChild, lst)

    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        # ---------- your code here ------------
        lst = []
        self.collect_leaf_nodes(self.root, lst)
        leaves = len(lst)
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
