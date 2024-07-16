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
    n, x = inlt()
    a = inlt()

    #exclusive r
    l = 0
    prod = 1
    res = 0
    for r in range(1, n + 1):
        print(f"l: {l} r: {r} prod: {prod}")

        prod *= a[r - 1]
        while prod > x and l < r:
            prod = prod // a[l]
            l += 1
        if prod == x:
            prod = a[r - 1]
            res += 1
            l = r - 1
        print(f"after l: {l} r: {r} prod: {prod}")

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

for i in range(100000):
    print(i)