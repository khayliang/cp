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

def postordering(adj):
    stk = deque([(0, 0)])
    order = deque()
    while stk:
        parent, curr = stk.pop()
        order.append((parent, curr))
        for x in adj[curr]:
            if x == parent:
                continue
            stk.append((curr, x))
    return order

def check(k, m, n, adj, sizes, postorder):
    # no. of components of size at least k and remaining
    amt = [[0, 0] for _ in range(n)]
    while postorder:
        parent, curr = postorder.pop()
        rem = 1
        for x in adj[curr]:
            if x == parent:
                continue
            rem += amt[x][1]
            amt[curr][0] += amt[x][0]
        if rem >= m:
            amt[curr][0] += 1
            rem = 0
        amt[curr][1] = rem
    if amt[0][0] > k:
        return True
    else:
        return False

# use yield to give ans. return to stop
def solve():
    n, k = inlt()
    adj = [[] for i in range(n)]
    for i in range(n - 1):
        v, u = inlt()
        adj[v - 1].append(u - 1)
        adj[u - 1].append(v - 1)

    postorder = postordering(adj)
    sizes = [1 for _ in range(n)]
    stk = deque(postorder)
    while stk: 
        parent, curr = stk.pop()
        for x in adj[curr]:
            if x == parent:
                continue

            sizes[curr] += sizes[x]
        
    # max component size possible is n // (k + 1)
    l, r = 0, n // (k)
    while l < r:
        m = (l + r + 1) // 2
        if check(k, m, n, adj, sizes, deque(postorder)):
            l = m
        else:
            r = m - 1
    yield l

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