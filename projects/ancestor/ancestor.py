from graph import Graph
def earliest_ancestor(ancestors, starting_node):
    """
    1.create a new graph
    2.loop through every tuple of values being pased in and add vertices for all values
    """
    g = Graph()
    for pair in ancestors:
        g.add_vertex(pair[0])
        g.add_vertex(pair[1])

        """
        loop through all tuples and add an edge from the value at index 0 to the value of index 1 
        """
    for pair in ancestors:
        g.add_edge(pair[1], pair[0])

