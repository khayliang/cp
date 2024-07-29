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
    
def ind(x):
    return ord(x) - ord("a")
# use yield to give ans. return to stop
def solve():
    n, q = inlt()
    a = insr()
    b = insr()
    da = [[0] for _ in range(ord("z") - ord("a") + 1)]
    db = [[0] for _ in range(ord("z") - ord("a") + 1)]
    N = ind("z") + 1

    for x in a:
        for i in range(N):
            if i == ind(x):
                da[i].append(da[i][-1] + 1)
            else:
                da[i].append(da[i][-1])
    for x in b:
        for i in range(N):
            if i == ind(x):
                db[i].append(db[i][-1] + 1)
            else:
                db[i].append(db[i][-1])
        
    for _ in range(q):
        l, r = inlt()
        a_amt = [da[i][r] - da[i][l - 1] for i in range(N)]
        b_amt = [db[i][r] - db[i][l - 1] for i in range(N)]
        amt = 0
        for i in range(N):
            amt += abs(a_amt[i] - b_amt[i])
        yield amt // 2
        
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