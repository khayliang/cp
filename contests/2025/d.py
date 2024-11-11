import sys
import math
import heapq
import bisect
from collections import deque, defaultdict
from itertools import permutations
from types import GeneratorType

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

############ ---- Function to Bootstrap Recursion ---- ############
"""
Add the decorator @bootstrap above the recursive function.
For the recursion to work, yield the recusive function.
Recursive function must yield something regardless
To return a value, add the line yield yield fn()
"""
def bootstrap(f, stack=deque()):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
    
# use yield to give ans. return to stop
def solve():
    n, m = inlt()
    r = inlt()
    a = []
    curr = 0
    for x in r:
        if x == 0:
            curr += 1
        else:
            if curr != 0:
                a.append((0, curr))
                curr = 0
            if x > 0:
                a.append((1, x))
            else:
                a.append((2, -x))
    if curr != 0:
        a.append((0, curr))
    dpi = [0 for _ in range(m + 1)]
    dps = [0 for _ in range(m + 1)]
    tot = 0
    for typ, amt in a:
        if typ == 0:
            tot += amt
        elif typ == 1: # int
            if amt <= tot:
                dpi[amt] += 1
        else:
            if amt <= tot:
                dps[amt] += 1
    ipf = [0]
    for x in dpi:
        ipf.append(ipf[-1] + x)
    spf = [0]
    for x in dps:
        spf.append(spf[-1] + x)
    res = []
    for i in range(m + 1):
        res.append(ipf[i + 1] + spf[m + 1 - i])
    
    print(max(res))


solve()