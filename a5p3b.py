"""
ECE606, F'19, Assignment 5, Problem 3b
Skeleton solution file.
"""

from a5p3bminnumcoins import minnumcoins

"""
You are not allowed to import anything else.
You need to implement the following method. You are
allowed to define whatever subroutines you like to
structure your code.
"""


def mincoinslist(C, a):
    """
        You need to implement this method.
        C is a list of coin values with C[0] = 1, and C[i] < C[i+1]
        a is a naural number
        """

    n = minnumcoins(C, a)
    if len(C) == 1:
        return [n]

    result = [0] * len(C)
    # To ensure the function will not change the value of C.
    C_1 = C.copy()
    for j in range(len(C) - 1):
        result[j] = medSearch(C_1, C[j], 0, minnumcoins(C_1, a), a)
        a = a - result[j] * C[j]
        C_1.remove(C[j])

    result[-1] = n - sum(result)
    return result


def medSearch(C, v, p, r, a):

    C_j = C.copy()
    C_j.remove(v)

    while p <= r:
        med = (p + r) // 2
        # If we don't need any other coins of such value, then med is the correct answer.
        if med + minnumcoins(C_j, (a - med * v)) == minnumcoins(C, a):
            return med
        # If we still need more coins of each value, then med is smaller than the correct result.
        elif med + minnumcoins(C, (a - med * v)) == minnumcoins(C, a):
            p = med + 1
        # Else med is too much for the coins.
        else:
            r = med - 1


# The method below is based on dynamic programming, however, I think it's not a polynominal-time function
# but a exponential-time function.

# def mincoinslist(C, a):
#     """
#     You need to implement this method.
#     C is a list of coin values with C[0] = 1, and C[i] < C[i+1]
#     a is a naural number
#     """
#
#     mincoins = {0: [0] * len(C)}
#
#     for i in range(1, a + 1):
#         mincoins[i] = [float('inf')] * len(C)
#         for j in range(len(C)):
#             if C[j] <= i and sum(mincoins[i - C[j]]) + 1 < sum(mincoins[i]):
#                 mincoins[i] = mincoins[i - C[j]].copy()
#                 mincoins[i][j] += 1
#
#     return mincoins[a]

