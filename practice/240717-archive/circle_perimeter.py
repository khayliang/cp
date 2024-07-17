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

############ ---- Output Functions ---- ############
def outlt(a):
    return " ".join(map(str, a))


# use yield to give ans. return to stop
def solve():
    r = inp()
    amt = 0
    for i in range(1, r + 1):
        k = int(((r + 1) * (r + 1) - i * i) ** (1/2)) + 1
        for j in range(k, -1, -1):
            rij = (j * j + i * i) ** (1/2)
            if rij >= r + 1:
                continue
            if rij >= r and rij < r + 1:
                amt += 1
                continue
            break

    amt = amt * 4
    yield amt
    
        

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