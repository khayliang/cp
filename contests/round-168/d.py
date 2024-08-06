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
    n = inp()
    a = [0] + inlt()
    parents = [1, 1] + inlt()
    adj = [[] for _ in range(n + 1)]
    for i, p in enumerate(parents):
        if i == 0 or i == 1:
            continue
        adj[p].append(i)

    @bootstrap
    def recurse(v, a, parents, adj):

        curr = a[v]
        
        if len(adj[v]) == 0:
            yield curr

        mn = INF
        for c in adj[v]:
            val = yield recurse(c, a, parents, adj)
            mn = min(mn, val)
        if curr > mn:
            yield mn
        else:
            yield (mn + curr) // 2
    
    mn = INF
    for c in adj[1]:
        val = recurse(c, a, parents, adj)
        mn = min(mn, val)

    yield mn + a[1]


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