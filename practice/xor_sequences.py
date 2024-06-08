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
    x, y = inlt()
    amt = 0
    while x & 1 == y & 1:
        amt += 1
        x = x >> 1
        y = y >> 1
    print(pow(2, amt))