import sys
from collections import deque, defaultdict
import math
import random

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

def sol(n, k):
    p = math.lcm(*k)

    res = [p//i for i in k]
    if sum(res) >= p:
        return -1
    
    return res

for _ in range(inp()):
    n = inp()
    k = inlt()
    res = sol(n, k)
    if res == -1:
        print(-1)
    else:
        print(*res)
