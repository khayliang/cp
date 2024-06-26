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

    first = a[0]
    last = a[-1]
    if first == last:
        yield "NO"
        return
    
    yield "YES"

    ans = "B"
    second = a[1]
    if second == first:
        yield "B" + ("R" * (n - 1))
    else:
        yield ("B" * (n - 1)) + "R"

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