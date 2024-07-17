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

############ ---- Output Parsing Functions ---- ############
def outlt(a):
    return " ".join(map(str, a))

# use yield to give ans. return to stop
def solve():
    n, c = inlt()
    a = inlt()
    a[0] += c
    mx = max(a)

    pf = [a[0]]
    for i in range(1, n):
        pf.append(a[i] + pf[-1])
    
    res = []

    first_mx = -1

    for i in range(n):
        if a[i] < mx:
            if pf[i] < mx:
                res.append(i + 1)
            else:
                res.append(i)
        elif a[i] == mx:
            if first_mx == -1:
                first_mx = i
                res.append(0)
            else:
                res.append(i)

    
    yield outlt(res)

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