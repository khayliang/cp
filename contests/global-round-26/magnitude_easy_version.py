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

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()

    mn = 0
    mx = 0
    for x in a:
        if x == 0:
            continue
        prev_mn = mn
        prev_mx = mx
        mn = min(prev_mn + x, abs(prev_mn + x), prev_mx + x, abs(prev_mx + x))
        mx = max(prev_mn + x, abs(prev_mn + x), prev_mx + x, abs(prev_mx + x))
    yield max(abs(mn), abs(mx))
        

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