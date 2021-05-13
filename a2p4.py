"""
ECE606, F'19, Assignment 2, Problem 4
Skeleton solution file.
"""

"""
You are not allowed to import anything.
You need to implement the following methods. You are
allowed to define whatever subroutines you like to
structure your code.
"""


def trieInsert(t, s):
    """
    You need to implement this method.
    """

    if not t:
        t += [[[], [], [], []], False]
    if not s:
        t[1] = True
        return
    for char in s[:-1]:
        if not t[0][int(char)]:
            t[0][int(char)] = [[[], [], [], []], False]
        t = t[0][int(char)]
    if not t[0][int(s[-1])]:
        t[0][int(s[-1])] = [[[], [], [], []], True]
    else:
        t = t[0][int(s[-1])]
        t[1] = True


def trieDelete(t, s):
    """
    You need to implement this method.
    """

    if not trieFind(t, s):
        return

    t1 = t
    for char in s:
        t1 = t1[0][int(char)]
    if not isLeaf(t1):
        t1[1] = False
        return
    t1.clear()

    while len(s) >= 0:
        s = s[:-1]
        t2 = t
        for char in s:
            t2 = t2[0][int(char)]
        if not (isLeaf(t2) and not t2[1]):
            return
        t2.clear()


def trieFind(t, s):
    """
    You need to implement this method.
    """

    if not t:
        return False
    if not s:
        return True if t[1] else False
    for char in s[:-1]:
        if t[0][int(char)]:
            t = t[0][int(char)]
        else:
            return False
    if t[0][int(s[-1])]:
        t = t[0][int(s[-1])]
        return True if t[1] else False
    else:
        return False

def isLeaf(t):
    try:
        if(len(t[0][0]) == 0 and len(t[0][1]) == 0 and len(t[0][2]) == 0 and len(t[0][3]) == 0):
            return True

        return False
    except:
        return False