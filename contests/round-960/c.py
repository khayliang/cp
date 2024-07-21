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
    n = inp()
    a = inlt()

    s = sum(a)

    mx = 0
    d = defaultdict(lambda: 0)
    b = []
    for x in a:
        d[x] += 1
        if d[x] > 1 and x > mx:
            mx = x
        b.append(mx)
    
    s += sum(b)
    a = b
    mx = 0
    d = defaultdict(lambda: 0)
    b = []
    for x in a:
        d[x] += 1
        if d[x] > 1 and x > mx:
            mx = x
        b.append(mx)

    amt = defaultdict(lambda: 0)
    ends = defaultdict(lambda: None)

    for i, x in enumerate(b):
        if i + 1 == n or b[i + 1] != x:
            ends[x] = i
        
        amt[x] += 1

    for v in amt:
        if amt[v] == 1:
            s += v
            continue

        s += ((n - ends[v] - 1) * amt[v] + (amt[v] * (amt[v] + 1)) // 2) * v
        
    yield s

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

test()