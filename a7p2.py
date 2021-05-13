"""
ECE606, F'19, Assignment 7, Problem 2
Skeleton solution file.
"""

"""
You are not allowed to import anything.
You need to implement the following method. You are
allowed to define whatever subroutines you like to
structure your code.
"""

def minncoins(C, N, a):
    """
    You need to implement this method.
    C is a list of coin values with len(C) > 0, C[0] = 1, C[i] < C[i+1]
    N is a list of number of each coin value
    a is an amount
    """

    mincoins = {0: [0] * len(C)}

    for i in range(1, a + 1):
        mincoins[i] = [float('inf')] * len(C)
        for j in range(len(C)):
            if C[j] <= i and sum(mincoins[i - C[j]]) + 1 < sum(mincoins[i]) and mincoins[i - C[j]][j] + 1 <= N[j]:
                mincoins[i] = mincoins[i - C[j]].copy()
                mincoins[i][j] += 1

    return sum(mincoins[a])
