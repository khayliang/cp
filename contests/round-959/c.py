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
    n, x = inlt()
    a = inlt()
    pf = [0]
    for i in a:
        pf.append(pf[-1] + i)
    res = [0 for _ in range(n)]
    for i in reversed(range(n)):
        if i == n - 1:
            if a[i] <= x:
                res[i] = 1
            else:
                res[i] = 0
            continue
        if a[i] > x:
            res[i] = res[i + 1]
            continue

        #index where you die
        j = bisect.bisect_right(pf, pf[i] + x, lo=i) - 1
        res[i] = j - i
        if j + 1 < n:
            res[i] += res[j + 1]
        
    yield sum(res)

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