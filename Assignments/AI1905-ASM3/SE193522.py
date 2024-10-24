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

    def preOrderRecursive(self, tmp, lst):
        if tmp != None:
            lst.append(tmp.key)
            self.preOrderRecursive(tmp.lChild, lst)
            self.preOrderRecursive(tmp.rChild, lst)
    def preOrderTraversal(self):
        """This is preorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self.preOrderRecursive(self.root, self._traversal_list)
        #-------------------------------------- 
        return self._traversal_list

    def inOrderRecursive(self, tmp, lst):
        if tmp != None:
            self.inOrderRecursive(tmp.lChild, lst)
            lst.append(tmp.key)
            self.inOrderRecursive(tmp.rChild, lst)


    def inOrderTraversal(self):
        """This is inorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self.inOrderRecursive(self.root, self._traversal_list)
        #-------------------------------------- 
        return self._traversal_list

    def postOrderRecursive(self, tmp, lst):
        if tmp != None:
            self.postOrderRecursive(tmp.lChild, lst)
            self.postOrderRecursive(tmp.rChild, lst)
            lst.append(tmp.key)

    def postOrderTraversal(self):
        """This is postorder traversal method.

        Returns:
            List(): a list consisted of all key nodes in the current tree
        """
        self._traversal_list = []
        #---------- your code here ------------
        self.postOrderRecursive(self.root, self._traversal_list)
        #-------------------------------------- 
        return self._traversal_list

    def search(self, key):
        """This method is used for searching key in the current tree
        """
        found = False
        #---------- your code here ------------
        search_lst = []
        self.postOrderRecursive(self.root, search_lst)
        if key in search_lst:
            found = True
        #-------------------------------------- 
        return found

    def parentKey(self, key):
        """This method is used to find key of parent node if it exists
        """
        parent_key = 0
        #---------- your code here ------------
        if self.root == None:
            return None
        tmp = self.root

        while tmp:
            if key < tmp.key:
                if tmp.lChild and key == tmp.lChild.key:
                    parent_key = tmp.key
                tmp = tmp.lChild
            else:
                if tmp.rChild and key == tmp.rChild.key:
                    parent_key = tmp.key
                tmp = tmp.rChild
        #-------------------------------------- 
        return parent_key
    
    def get_height(self):
        """This method is used to get the height of the current tree

        Returns:
            unsigned int: the height of tree
        """
        height = 0
        #---------- your code here ------------
        def cal_height(tmp):
            if tmp is None:
                return -1
            left_height = cal_height(tmp.lChild)
            right_height = cal_height(tmp.rChild)
            return max(left_height, right_height) + 1
        height = cal_height(self.root)
        #-------------------------------------- 
        return height

    def countRecursive(self, tmp, lst):
        if tmp != None:
            if tmp.lChild is None and tmp.rChild is None:
                lst.append(tmp.key)
            self.countRecursive(tmp.lChild, lst)
            self.countRecursive(tmp.rChild, lst)
    def count_leaves(self):
        """This method is used to all leaves of the current tree
        """
        leaves = 0
        #---------- your code here ------------
        lst_leaves = []
        self.countRecursive(self.root, lst_leaves)
        leaves = len(lst_leaves)
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
    
    k = 20
    if (t.search(k)):
        print("\nNode ", k, " is in the BSTree")
    else:
        print("\nNode ", k, " is not in the BSTree")
        
    print("\nParent key of 20 :  ", t.parentKey(20))
    print("\nAmount of leaf Nodes:  ", t.count_leaves())
    print("\nHeight of the tree:  ", t.get_height())