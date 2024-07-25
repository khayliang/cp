import sys
import math
from collections import deque, defaultdict
from itertools import permutations
import bisect
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
def bootstrap(f, stack=[]):
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

def find_bridges(adj):
    n = len(adj)
    t = [float('inf') for _ in range(n)]
    earliest = [float('inf') for _ in range(n)]
    index = [0]
    sizes = [1 for _ in range(n)]
    bridges = []

    @bootstrap
    def dfs(adj, curr=0, parent=0, index=index, t=t, earliest=earliest, bridges=bridges, sizes=sizes):
        ind = index[0]
        t[curr] = ind

        if len(adj[curr]) == 0:
            earliest[curr] = ind
            yield
        
        for c in adj[curr]:
            if c == parent:
                continue

            if t[c] < float('inf'):
                earliest[curr] = min(earliest[curr], t[c])
                continue

            index[0] += 1
            yield dfs(adj, c, curr, index, t, earliest, bridges, sizes)
            earliest[curr] = min(earliest[curr], earliest[c])
            if t[curr] < earliest[c]:
                bridges.append((curr, c))
        
        for c in adj[curr]:
            if c == parent:
                continue
            sizes[curr] += sizes[c]
            
        yield

    dfs(adj)

    return bridges
    

# use yield to give ans. return to stop
def solve():
    n, m = inlt()
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = inlt()
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    t = [float('inf') for _ in range(n)]
    earliest = [float('inf') for _ in range(n)]
    index = [0]
    sizes = [1 for _ in range(n)]
    bridges = []

    @bootstrap
    def dfs(adj, curr=0, parent=0, index=index, t=t, earliest=earliest, bridges=bridges, sizes=sizes):
        ind = index[0]
        t[curr] = ind

        if len(adj[curr]) == 0:
            earliest[curr] = ind
            yield
        
        for c in adj[curr]:
            if c == parent:
                continue

            if t[c] < float('inf'):
                earliest[curr] = min(earliest[curr], t[c])
                continue

            index[0] += 1
            yield dfs(adj, c, curr, index, t, earliest, bridges, sizes)
            earliest[curr] = min(earliest[curr], earliest[c])
            sizes[curr] += sizes[c]

            if t[curr] < earliest[c]:
                bridges.append((curr, c))
            
            
        yield

    dfs(adj)

    res = float('inf')
    if len(bridges) == 0:
        yield math.comb(n, 2)
        return

    for _, v in bridges:
        if sizes[v] > 1 and n - sizes[v] > 1:
            res = min(res, math.comb(sizes[v], 2) + math.comb(n - sizes[v], 2))
        else:
            res = min(res, math.comb(max(sizes[v], n - sizes[v]), 2))
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

submit()