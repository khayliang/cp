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
    c = sorted(a)
    lower_med = c[n // 2 - 1]
    higher_med = c[n // 2]
    d = []
    for i in range(n):
        if b[i] == 1 and a[i] <= lower_med:
            d.append(a[i])
    d.sort()
    if not d:
        return c[-1] + lower_med        
    
    val = d[-1]
    if d[-1] + k >= higher_med:
        k -= higher_med - val
        val = higher_med
    else:
        val = d[-1] + k
    if k > 0 and len(d) > 2 and if :
        d[-2] + val
    if val > higher_med

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