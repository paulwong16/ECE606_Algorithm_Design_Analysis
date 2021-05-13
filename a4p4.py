"""
ECE606, F'19, Assignment 4, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything.
You need to implement the following method. You are
allowed to define whatever subroutines you like to
structure your code.
"""

def negcycle(G):
    """
    You need to implement this method.
    The input A is a directed graph encoded as
    a list of lists of <neighbour, weight> pairs.
    """

    res = []
    width = len(G)
    isVis = [0] * width
    for i in range(width):
        result = []
        weight = 0
        path = [i]
        if isVis[i] == 0:
            isCir = dfs(G, i, isVis, weight, path, result)
            if isCir == 0:
                for p in result:
                    if 3 < len(p) <= 8:
                        res.append(p)
    return res


def dfs(G, i, isVis, weight, path, res):
    isVis[i] = -1
    isCir = 1
    for edge in G[i]:
        if isVis[edge[0]] == -1:
            path.append(edge[0])
            path_to_add = path.copy()
            # [weight_1, path_new] = loop_detect(path_to_add, G, weight + edge[1])
            path_new = loop_detect(path_to_add)
            if path_new:
                res += [path_new]
                isCir = 0
                return isCir
            path.pop()
        elif isVis[edge[0]] == 0:
            weight += edge[1]
            path.append(edge[0])
            isCir = dfs(G, edge[0], isVis, weight, path, res)
    path.pop()
    isVis[i] = 0
    return isCir


# def loop_detect(path, G, weight):
#     new_weight = weight
#     path_new = path.copy()
#     for i in range(len(path)):
#         if path[i] != path[-1]:
#             path_new.remove(path[i])
#             for j in G[path[i]]:
#                 if path[i+1] == j[0]:
#                     new_weight -= j[1]
#         else:
#             break
#     return [new_weight, path_new]


def loop_detect(path):
    # new_weight = weight
    path_new = path.copy()
    for i in range(len(path)):
        if path[i] != path[-1]:
            path_new.remove(path[i])
            # for j in G[path[i]]:
            #     if path[i+1] == j[0]:
            #         new_weight -= j[1]
        else:
            break
    return path_new
