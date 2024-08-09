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
    n, m = inlt()
    a = inlt()
    b = inlt()
    C = inlt()
    mxa = max(a)
    best = [INF for _ in range(mxa + 1)]
    for i in range(n):
        v, s = a[i], b[i]
        best[v] = min(v - s, best[v])
    for i in range(1, mxa + 1):
        best[i] = min(best[i], best[i - 1])
    scores = [INF for _ in range(mxa + 1)]
    for i in range(1, mxa + 1):
        if best[i] == INF:
            continue
        if scores[i - best[i]] == INF:
            scores[i] = 1
        else: 
            scores[i] = 1 + scores[i - best[i]]
    res = 0
    for c in C:
        if c <= mxa:
            if scores[c] != INF:
                res += scores[c]
        else:
            steps = ((c - mxa) // best[mxa]) + 1
            rem = c - (steps * best[mxa])
            res += steps
            if scores[rem] != INF:
                res += scores[rem]

    yield res * 2
def test():
    ans = []
    for a in solve():
        ans.append(a)
    for i in ans:
        print(i)

def submit():
    for a in solve():
        print(a)

submit()