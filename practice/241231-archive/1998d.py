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
    adj = [[i + 1] if i < n else [] for i in range(n + 1)]
    radj = [[i - 1] if i > 1 else [] for i in range(n + 1)]

    for _ in range(m):
        u, v = inlt()
        adj[u].append(v)
        radj[v].append(u)
    
    mpjt = [0] * (n + 1)
    mj = 0
    res = []
    for s in range(n - 1):
        for z in radj[s]:
            mpjt[s] = max(mpjt[s], mpjt[z] + s - z - 1)
        for z in adj[s]:
            mj = max(mj, mpjt[s] + z - s - 1)
        res.append("0" if mj > s else "1")
    print(mpjt[1:])

    yield "".join(res)
    

    

    
    
        

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