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
    n = int(input())
    x, y, z, w = 0, 0, 0, 0
    deg = [0] * (n + 1)
    for __ in range(n - 1) :
        u, v = map(int, input().split())
        deg[u] += 1
        deg[v] += 1
    s = " " + input()
    for i in range(2, n + 1) :
        if deg[i] == 1 :
            if s[i] == '?' :
                z += 1
            elif s[i] == '0' :
                x += 1
            else :
                y += 1
        elif s[i] == '?' :
            w += 1
    if s[1] == '0' :
        yield (y + (z + 1) // 2)
    elif s[1] == '1' :
        yield (x + (z + 1) // 2)
    else :
        yield (max(x, y) + (z + (w % 2 if x == y else 0)) // 2)


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