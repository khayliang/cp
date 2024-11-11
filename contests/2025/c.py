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
    n, k = inlt()
    a = inlt()
    count = defaultdict(lambda: 0)
    for x in a:
        count[str(x)] += 1

    d = sorted(list(set(a)))
    l, r = 0, 0
    curr = 0
    curr_amt = 1
    mx = 0
    while l != len(d):
        curr += count[str(d[r])]
        mx = max(curr, mx)
        if r + 1 == len(d):
            break
        if d[r + 1] == d[r] + 1:
            r += 1
            if curr_amt == k:
                curr -= count[str(d[l])]
                l += 1
            else:
                curr_amt += 1
        else:
            curr_amt = 1
            curr = 0
            r += 1
            l = r
    yield mx
    
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