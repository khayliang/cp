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
    x, y, z, k = inlt()
    
    best = 0
    for a in range(1, x + 1):
        for b in range(1, y + 1):
            if (k % (a * b)) != 0:
                continue
            c = int(k / (a * b))
            best = max(best, (x - a + 1) * (y - b + 1) * (z - c + 1))
    yield best

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