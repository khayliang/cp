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
    n, m, k = inlt()
    a = insr()
    
    c = k
    j = m
    for x in a:
        if j > 0:
            j -= 1
        elif c > 0:
            c -= 1

        if x == "L":
            j = m

        elif x == "C":
            if j == 0:
                yield "NO"
                return

        else:
            if c == 0 and j == 0:
                yield "NO"
                return

    if c == 0 and j == 0:
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