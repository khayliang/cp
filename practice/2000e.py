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
    n, m, k = inlt()
    w = inp()
    a = inlt()
    a.sort(reverse=True)
    d = defaultdict(lambda: 0)

    mx = 0
    score = []
    for i in range(n):
        for j in range(m):
            amt = (max(((min(n - 1, i + k - 1) - max(0, i - k + 1))), 1) * max(1, ((min(m - 1, j + k - 1) - max(0, j - k + 1)))))
            print(i, j, amt, (min(n - 1, i + k - 1) - max(0, i - k + 1)), (min(m - 1, j + k - 1) - max(0, j - k + 1)))
            mx = max(amt, mx)
            score.append(amt)
    score.sort()
    print(score)

    score = deque(score)
    res = 0
    for i, x in enumerate(a):
        mx = score.pop()
        res += x * mx
    yield res

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