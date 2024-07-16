import sys
from collections import deque, defaultdict
from itertools import permutations

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

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = [0] + inlt()

    if n == 1:
        yield a[1]
        return

    adj = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        x, y = inlt()
        adj[x].append(y)
        adj[y].append(x)

    root = 1
    evens = 0
    odds = 0

    visited = [False for _ in range(n + 1)]
    visited[root] = True

    stk = deque([(root, 0)])

    while stk:
        curr, depth = stk.popleft()

        if depth % 2 == 0:
            evens += a[curr]
        else:
            odds += a[curr]
        
        for x in adj[curr]:
            if not visited[x]:
                stk.append((x, depth + 1))
                visited[x] = True
    
    tot = sum(a)
    if evens > odds:
        yield tot + odds
    else:
        yield tot + evens
    
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