"""
ECE606, F'19, Assignment 9, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything.
You need to implement the following method. You are
allowed to define whatever subroutines you like to
structure your code.
"""

def hampath(G):
    """
    You need to implement this method
    """

    for i in range(len(G)):
        path = [-1] * len(G)
        path[0] = i
        if hamPathUtil(G, path, 1):
            return path
    return []


def hamPathUtil(G, path, pos):
    if pos == len(G):
        return True
    for v in G[path[pos-1]]:
        if v not in path:
            path[pos] = v
            if hamPathUtil(G, path, pos+1):
                return True
            path[pos] = -1
    return False
