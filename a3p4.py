"""
ECE606, F'19, Assignment 3, Problem 4
Skeleton solution file.
"""

import random

"""
You are not allowed to import anything else.
You need to implement the following method. You are
allowed to define whatever subroutines you like to
structure your code.
"""

def avgtrials(A):
    """
    You need to implement this method.
    The input A is a list of distinct integers,
    whose size is an odd number.
    """
    result = 0
    for i in range(0, 100):
        result = result + med(A)

    return result / 100


def med(A):
    if len(A) % 2 == 0:
        return 0
    n = len(A)
    s = list(range(0, n))
    counter = 0
    while True:
        i = random.choice(s)
        counter = counter + 1
        if check_if_median(i, A):
            return counter
        s.remove(i)


def check_if_median(i, A):
    m = len(A) // 2
    A_sort = A.copy()
    A_sort.sort()
    return True if A[i] == A_sort[m] else False
