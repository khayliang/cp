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

    mx = 0
    sm = 0
    a.sort()
    l = 0
    for r in range(n):
        x = a[r]
        prev = a[l]

        if x > m:
            break
        
        sm += x
        
        if x != prev and x - 1 != prev:
            while a[l] < a[r] - 1:
                sm -= a[l]
                l += 1

        while sm > m and l < r:
            sm -= a[l]
            l += 1

        mx = max(sm, mx)

    yield mx


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