"""
ECE606, F'19, Assignment 6, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything.
You need to implement the following method. You are
allowed to define whatever subroutines you like to
structure your code.
"""

def mstexists(G, e):
    """
    You need to implement this method.
    G is an adjacency list in the format discussed in the handout
    e is a list of two items, e.g., [0,4]
    """

    vertex_list = [0]
    edge_list = []

    while len(vertex_list) != len(G):
        for vertex in vertex_list:
            for edge in G[vertex]:
                if edge[0] not in vertex_list:
                    edge_to_add = sorted([vertex, edge[0]])
                    edge_to_add.append(edge[1])
                    if edge_to_add not in edge_list:
                        edge_list.append(edge_to_add)
        edges_to_remove = findminedge(edge_list)  # Kruskal's algorithm
        for edge_to_remove_list in edges_to_remove:
            if sorted(e) == edge_to_remove_list[0:2]:
                return True
        # if sorted(e) == edge_to_remove[0:2]:
        #     return True
        edge_to_remove = edges_to_remove[0]
        edge_list.remove(edge_to_remove)
        vertex_list.append(edge_to_remove[1]) if edge_to_remove[0] in vertex_list else vertex_list.append(edge_to_remove[0])
        edge_list_cp = edge_list.copy()
        for edge_remain in edge_list:
            if edge_remain[0] in vertex_list and edge_remain[1] in vertex_list:
                edge_list_cp.remove(edge_remain)
        edge_list = edge_list_cp.copy()

    return False


def findminedge(edge_list):
    edge_list.sort(key=lambda x: x[2])
    res = [edge_list[0]]
    for edge in edge_list:
        if edge[2] == edge_list[0][2]:
            res.append(edge)
    return res
