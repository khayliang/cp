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
    seg = [inlt(), inlt()]
    seg.sort(key=lambda x: x[0])
    if seg[0][1] < seg[1][0]:
        yield 1
        return
    
    overlap = 0
    for i in range(seg[0][0], seg[0][1] + 1):
        if i >= seg[1][0] and i <= seg[1][1]:
            overlap += 1
    overlap += 1
    if seg[0][0] == seg[1][0]:
        overlap -= 1
    if seg[0][1] == seg[1][1]:
        overlap -= 1
    yield overlap


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