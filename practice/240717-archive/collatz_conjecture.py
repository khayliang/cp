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
    x, y, k = inlt()
    while k != 0:
        if x == 1:
            yield 1 + (k % (y - 1))
            return
        to_mult = (((x // y) + 1) * y) - x
        if to_mult <= k:
            k -= to_mult
        else:
            x += k
            break
        x += to_mult
        while x % y == 0:
            x = x // y
    yield x
        
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