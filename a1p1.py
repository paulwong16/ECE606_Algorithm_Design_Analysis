"""
ECE606, F'19, Assignment 1, Problem 3(b)
Skeleton solution file.
"""

import random
"""
You are not allowed to import anything else
"""

def avgfalsepos(n,k,m):
    """
    You need to implement this method.
    You are certainly allowed to define any subroutines you want
    above this method in this file. You are not, however, allowed
    to import any more packages than already imported above.
    """

    # check if k is not greater than n.
    if k > n or k < 1:
        return 0

    result = 0

    # run 100 uniform functions.
    for i in range(100):
        # the probability that B[i] is still 0 after inserting k members.
        pr_0 = pow((1 - (1 / m)), k)
        # the probability that B[i] is 1 after inserting k members.
        pr_1 = 1 - pr_0
        # the false positive numbers should be (n-k) * pr_1. (n-k) denotes |U|-|S|
        result = (n-k) * pr_1

    return result
