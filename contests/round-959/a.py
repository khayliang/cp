import sys
import math
from collections import deque, defaultdict
from itertools import permutations

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
    n, m = inlt()
    mat = [inlt() for _ in range(n)]

    if n == 1 and m == 1:
        yield -1
        return
    
    if m == 1:
        for i in range(n):
            if i == 0:
                yield mat[n - 1][0]
            else:
                yield mat[i - 1][0]
        return
    
    for r in mat:
        yield outlt([r[-1]] + r[0:m - 1])
    return

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