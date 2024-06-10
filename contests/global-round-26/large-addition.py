import sys
from collections import deque, defaultdict
from math import log10
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
    x = inp()
    n = int(log10(x)) + 1
    for i in range(n):
        d = x % 10
        if i == 0 and d > 8:
            yield "NO"
            return
        elif i == n - 1:
            if d != 0:
                yield "NO"
                return
        elif d > 8:
            yield "NO"
            return

        x = x // 10
        x -= 1
    yield "YES"
    return



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