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
    parent = [None for _ in range(n + 1)]
    for i in range(1, n):
        x, y = i, n
        prev_y = y
        while y != x:
            yield f"? {x} {y}"
            prev_y = y
            y = inp()
        parent[x] = prev_y
    
    res = []
    said = set()
    for x in range(1, n):
        edge = sorted([x, parent[x]])
        if outlt(edge) not in said:
            res += edge
            said.add(outlt(edge))
    yield "! " + outlt(res)
            


def test():
    ans = []
    for _ in range(inp()):
        for a in solve():
            ans.append(a)
    for i in ans:
        print(i)
        sys.stdout.flush()


def submit():
    for _ in range(inp()):
        for a in solve():
            print(a)
            sys.stdout.flush()


submit()