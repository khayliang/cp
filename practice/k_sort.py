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
    a = inlt()
    mx = 0
    k = []
    for x in a:
        if mx == 0:
            mx = x
            continue
        
        if x < mx:
            k.append(mx - x)
        else:
            mx = x

    k.sort()
    prev = 0
    res = 0

    for i, x in enumerate(k):
        if prev == x:
            continue

        res += (x - prev) * (len(k) - i + 1)
        prev = x
    
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