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
adj = [-1 for i in range(n + 1)]
parents = [-1 for i in range(n + 1)]

for _ in range(n - 1):
    u, v = inlt()

    parents[v] = u
    adj[u] = v

curr = 0
for i, x in enumerate(parents):
    if i == 0:
        continue

    if x == -1:
        curr = i
        break

imap = [-1 for i in range(n + 1)]

for i in range(1, n + 1):
    imap[curr] = i
    curr = adj[curr]

i = imap[inp()]

if (i - 1) % 2 == 1 or (n - i) % 2 == 1:
    print("Ron")
else:
    print("Hermione")

