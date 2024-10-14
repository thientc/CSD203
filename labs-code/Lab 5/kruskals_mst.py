def kruskals_mst(self):
    # Resulting tree
    result = []
    
    # Iterator
    i = 0
    # Number of edges in MST
    e = 0

    # Sort edges by their weight
    self.m_graph = sorted(self.m_graph, key=lambda item: item[2])
    
    # Auxiliary arrays
    parent = []
    subtree_sizes = []

    # Initialize `parent` and `subtree_sizes` arrays
    for node in range(self.m_num_of_nodes):
        parent.append(node)
        subtree_sizes.append(0)

    # Important property of MSTs
    # number of egdes in a MST is 
    # equal to (m_num_of_nodes - 1)
    while e < (self.m_num_of_nodes - 1):
        # Pick an edge with the minimal weight
        node1, node2, weight = self.m_graph[i]
        i = i + 1

        x = self.find_subtree(parent, node1)
        y = self.find_subtree(parent, node2)

        if x != y:
            e = e + 1
            result.append([node1, node2, weight])
            self.connect_subtrees(parent, subtree_sizes, x, y)
    
    # Print the resulting MST
    for node1, node2, weight in result:
        print("%d - %d: %d" % (node1, node2, weight))