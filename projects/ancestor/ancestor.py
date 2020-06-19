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

    """
    call the modified DFS function on the graph class
    finding the earliest ancestor for the starting node passed in 
    """
    ancestor = g.find_earliest_ancestor(starting_node)

    """
    if the last value in the list is the starting node there is no earliest ancestor for the start node to pass in 
    we return a -1 to show a failure 
    """
    if ancestor[-1] == starting_node:
        return -1
    # here we are getting back the last element in the list if out start node dose not have an earliest ancestor
    else:
        return ancestor[-1]
 if __name__ == "__main__":
     ancestors = [(1,3), (2,3), (3,6)]