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
def solve1(n, k, a, b):
    mx_idx = -1
    mx = -1
    for i in range(n):
        if b[i] == 1:
            if a[i] > mx:
                mx_idx = i
                mx = a[i]
    if mx_idx != -1:
        a[mx_idx] += k
    a.sort()
    if len(a) == 2:
        return sum(a)
    
    return a[-1] + a[n // 2 - 1]

def solve2(n, k, a, b):
    l = 0
    h = int(2e9)
    c = list(zip(a, b))
    c.sort(key=lambda x: x[0])
    while l < h:
        # for m to be the median, we need ((n - 1) // 2) + 1 numbers >= m
        m = (l + h + 1) // 2
        higher = 0
        lowers_diff = []
        for i in range(n - 1):
            if c[i][0] >= m:
                higher += 1
            elif c[i][1] == 1:
                lowers_diff.append(m - c[i][0])
        lowers_diff.sort()
        kk = k
        for x in lowers_diff:
            if x <= kk:
                kk -= x
                higher += 1
            else:
                break
        if higher >= ((n + 1) // 2):
            l = m
        else:
            h = m - 1
    return max(a) + l


def solve():
    n, k = inlt()
    a = inlt()
    b = inlt()
    ans1 = solve1(n, k, list(a), b)
    ans2 = solve2(n, k, a, b)
    yield max(ans1, ans2)

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