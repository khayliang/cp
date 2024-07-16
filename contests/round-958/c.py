import sys
from collections import deque, defaultdict
from itertools import permutations
import math

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


# use yield to give ans. return to stop
def solve():
    n = inp()
    res = [n]
    i = 0
    mx = math.log2(n)
    for i in range(int(math.log2(n)) + 1):
        v = 1 << i
        if n ^ v != n and n ^ v < res[-1] and  n ^ v > 0:
            res.append(n ^ v)
    yield len(res)
    yield outlt(list(reversed(res)))


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