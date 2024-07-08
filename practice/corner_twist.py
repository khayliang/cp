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
    n, m = inlt()
    prob = [list(map(int, insr())) for _ in range(n)]
    sol = [list(map(int, insr())) for _ in range(n)]

    for i in range(n):
        if sum(prob[i]) % 3 != sum(sol[i]) % 3:
            yield "NO"
            return
    
    for j in range(m):
        prob_sm = 0
        sol_sm = 0
        for i in range(n):
            prob_sm += prob[i][j]
            sol_sm += sol[i][j]
        if prob_sm % 3 != sol_sm % 3:
            yield "NO"
            return

    yield "YES"

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