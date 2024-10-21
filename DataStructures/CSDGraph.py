class CSDVetex:
    """_summary_
    """
    __slots__ = "_element"

    def __init__(self, element) -> None:
        self._element = element
    
    def get_element(self):
        return self._element
    
    def __hash__(self):
        return hash(self._element)
    
    def __eq__(self, other):
        return self._element == other.get_element()

    
class CSDEdge:
    __slots__ = "org_vertex", "dest_vertex"
    """_summary_
    """
    def __init__(self, org_vertex:CSDVetex, dest_vertex:CSDVetex) -> None:
        self.org_vertex = org_vertex
        self.dest_vertex = dest_vertex
    
    def opposite(self, vertex):
        if vertex == self.org_vertex:
            return self.dest_vertex
        if vertex == self.dest_vertex:
            return self.org_vertex
        return None
    
    def endpoints(self):
        return (self.org_vertex, self.dest_vertex)
    
    
class CSDGraph:
    """_summary_
    """
    __slots__ = "vertices_set", "edges_set"
    
    def __init__(self) -> None:
        self.vertices_set = set()
        self.edges_set = set()
        
    def add_vertex(self, vertex):
        self.vertices_set.add(vertex)

    def add_edge(self, edge:CSDEdge):
        endpoinds = edge.endpoints()
        self.add_vertex(endpoinds[0])
        self.add_vertex(endpoinds[1])
        self.edges_set.add(edge)
        
    def get_edge(self, u:CSDVetex, v:CSDVetex)->CSDEdge:
        for edge in self.edges():
            if edge[0] == u and edge[1] == v:
                return edge
        return None
    
    def vertex_count(self):
        return len(self.vertices_set)
    
    def vertices(self):
        return list(self.vertices_set)
    
    def degree(self,v):
        if v not in self.vertices_set:
            return None
        # degree = 0
        # for edge in self.edges():
        #     if v == edge.endpoints()[0] or v == edge.endpoints()[1]:
        #         degree +=1
        return len(self.incident_edges(v))
        # return degree
    
    def edges_count(self):
        return len(self.edges_set)
    
    def edges(self):
        return list(self.edges_set)
    
    def incident_edges(self, v):
        edge_list = []
        for edge in self.edges():
            if v == edge.endpoints()[0] or v == edge.endpoints()[1]:
                edge_list.append(edge)
        return edge_list
        
def make_graph_from_edges(mygraph:CSDGraph, list_of_edges):
    
    for edge_elements in list_of_edges:
        org_vertex = CSDVetex(edge_elements[0])
        dest_vertex = CSDVetex(edge_elements[1])
        edge = CSDEdge(org_vertex, dest_vertex)
        mygraph.add_edge(edge)
    pass

def DFS(g, u, discovered):
  """Perform DFS of the undiscovered portion of Graph g starting at Vertex u.

  discovered is a dictionary mapping each vertex to the edge that was used to
  discover it during the DFS. (u should be "discovered" prior to the call.)
  Newly discovered vertices will be added to the dictionary as a result.
  """
  for e in g.incident_edges(u):    # for every outgoing edge from u
    v = e.opposite(u)
    if v not in discovered:        # v is an unvisited vertex
      discovered[v] = e            # e is the tree edge that discovered v
      DFS(g, v, discovered)        # recursively explore from v

def construct_path(u, v, discovered):
  """
  Return a list of vertices comprising the directed path from u to v,
  or an empty list if v is not reachable from u.

  discovered is a dictionary resulting from a previous call to DFS started at u.
  """
  path = []                        # empty path by default
  if v in discovered:
    # we build list from v to u and then reverse it at the end
    path.append(v)
    print("append ", v.get_element())
    walk = v
    while walk != u:
      e = discovered[walk]         # find edge leading to walk
      parent = e.opposite(walk)
      path.append(parent)
      walk = parent
    path.reverse()                 # reorient path from u to v
  return path

if __name__ == "__main__":
    list_of_edges = [
        ("A", "B"), ("A", "F"), ("A", "E"), 
        ("B", "C"), ("F", "E"), ("B", "F"),
        ("E", "I"), ("F", "I"), 
        ("C", "D"), ("C", "G"), ("G", "D"),
        ("G", "J"), ("I", "J"), ("G", "K"),("G", "L"), 
        ("D", "H"), ("H", "L"), ("K", "J"),
        ("L", "P"), ("K", "O"), ("K", "N"), 
        ("I", "M"), ("I", "N"), ("N", "M"),
        ]
    mygraph = CSDGraph()
    make_graph_from_edges(mygraph, list_of_edges)
    # for v in mygraph.vertices():
    #     print(v.get_element())
        
    G = CSDVetex("G")
    K = CSDVetex("K")
    print(mygraph.degree(K))
    discovered = dict()
    
    A = CSDVetex("A")
    discovered[A] = None
    DFS(mygraph, A, discovered )
    path_A_G = construct_path(A, K, discovered)
    for v in path_A_G:
        print(v.get_element())
