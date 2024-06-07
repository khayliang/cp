import sys
from collections import deque, defaultdict

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

for _ in range(inp()):
    n = inp()
    a = inlt()
    mn = float('inf')
    for i in range(n - 1):
        mn = min(mn, max(a[i], a[i + 1]))
    print(mn - 1)

