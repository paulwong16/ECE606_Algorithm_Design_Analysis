"""
ECE606, F'19, Assignment 12, Problem 4
Skeleton solution file.
"""

import math # for things like log() and pow()


"""
You are not allowed to import anything else.
You need to implement the following method. You are
allowed to define whatever subroutines you like to
structure your code.
"""

def buildBST(A):
    """
    You need to implement this method
    """
    A.sort()  # o(nlogn)
    B = A.copy()  # o(n)
    l = len(A)  # o(1)
    stack = [[0, l - 1]]  # o(1)
    for i in range(l):  # n times
        idx = find_root(stack[i])  # o(1)
        A[i] = B[stack[i][0] + idx]  # o(1)
        if idx > 0:  # o(1)
            stack.append([stack[i][0], stack[i][0] + idx - 1])  # o(1)
            stack.append([stack[i][0] + idx+1, stack[i][1]])  # o(1)


def find_root(idx):  # o(1)
    length = idx[1] - idx[0] + 1
    level = math.floor(math.log2(length)) + 1
    last_level_num = length - pow(2, level - 1) + 1
    if level == 1:
        return 0
    if last_level_num <= pow(2, level-2):
        return pow(2, level-2) + last_level_num - 1
    else:
        return pow(2, level-1) - 1


"""
def buildBST(A):

    A.sort()  # o(nlogn)
    l = len(A)  # o(1)
    stack = [A.copy()]  # o(n)
    for i in range(l):  # n times o(n^2)
        idx = find_root(stack[i])
        A[i] = stack[i][idx]
        if stack[i][:idx]:
            stack.append(stack[i][:idx])  # o(n) !!!
        if stack[i][idx+1:]:
            stack.append(stack[i][idx+1:])  # o(n) !!!


def find_root(arr):  # o(1)
    length = len(arr)
    level = math.floor(math.log2(length)) + 1
    last_level_num = length - pow(2, level - 1) + 1
    if level == 1:
        return 0
    if last_level_num <= pow(2, level-2):
        return pow(2, level-2) + last_level_num - 1
    else:
        return pow(2, level-1) - 1
"""

"""
def buildBST_pop(A):

    A.sort()  # o(nlogn)
    stack = [A.copy()]  # o(n)
    while stack:  # o(n^2)
        idx = find_root(stack[0])
        A[0] = stack[0][idx]
        if stack[0][:idx]:
            stack.append(stack[0][:idx])
        if stack[0][idx + 1:]:
            stack.append(stack[0][idx + 1:])
        stack.pop(0)
"""