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

n, t = inlt()

adj = [[] for _ in range(n)]
parents = [-1 for _ in range(n)]
for i in range(n - 1):
    u, v = inlt()
    u -= 1
    v -= 1
    adj[u].append(v)
    adj[v].append(u)

k = inp()

curr = k - 1
visited = [False for _ in range(n)]
winner = [None for _ in range(n)]

def dfs(curr, ron):
    visited[curr] = True
    for x in adj[curr]:
        if not visited[x] and ron and dfs(x, not ron):
            return True
        if not visited[x] and not ron and not dfs(x, not ron):
            return False
    return not ron
        
if dfs(curr, True):
    print("Ron")
else:
    print("Hermione")


