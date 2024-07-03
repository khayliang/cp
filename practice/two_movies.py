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
    b = inlt()

    mv1 = 0
    mv2 = 0

    for i in range(n):
        if a[i] > b[i]:
            mv1 += a[i]
        elif a[i] < b[i]:
            mv2 += b[i]
    
    for i in range(n):
        if a[i] == b[i]:
            if a[i] == -1:
                if mv1 >= mv2:
                    mv1 += a[i]
                else:
                    mv2 += b[i]
            if a[i] == 1:
                if mv1 >= mv2:
                    mv2 += b[i]
                else:
                    mv1 += a[i]

    yield min(mv1, mv2)


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