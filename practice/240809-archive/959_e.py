import sys
import math
from collections import deque, defaultdict
from itertools import permutations
import random

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
    k = inp()
    ans = 0
    sizes = []
    for _ in range(k):
        sizes.append(inp())
        inlt()

    sizes.sort(reverse=True)

    for x in sizes:
        for h in range(23, -1, -1):
            ca = (ans >> h) & 1
            cx = (x >> h) & 1
            if cx == 0:
                continue
            if ca == 0:
                ans |= 1 << h
            else:
                ans |= (1 << h) - 1
                break
    
    yield ans

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