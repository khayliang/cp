import sys
import math
from collections import deque, defaultdict
from itertools import permutations
import bisect

input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

############ ---- Output Functions ---- ############
def outlt(a):
    return " ".join(map(str, a))

############ ---- Constants ---- ############
INF = float('inf')

# use yield to give ans. return to stop
def solve():
    n, x, y = inlt()
    res = [0 for _ in range(n)]

    for i in range(y - 1, x):
        res[i] = 1

    for i in range(y - 2, -1, -1):
        if (y - 2 - i) % 2 == 0:
            res[i] = -1
        else:
            res[i] = 1

    for i in range(x, n):
        if (i - x) % 2 == 0:
            res[i] = -1
        else:
            res[i] = 1

    yield outlt(res)


def test():
    ans = []
    for _ in range(inp()):
        for a in solve():
            ans.append(a)
    for i in ans:
        print(i)

def submit():
    for _ in range(inp()):
        for a in solve():
            print(a)

submit()