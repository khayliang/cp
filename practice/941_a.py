import sys
import math
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

############ ---- Constants ---- ############
INF = float('inf')

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()
    a.sort()
    acc = 0
    turns = 0
    for i, x in enumerate(a):
        print(turns)
        if x == acc:
            continue

        if x - acc == 1:
            turns += 1
            acc = x
            continue

        if (n - i) % 2 != 0:
            turns += 2
        else:
            turns += 1
        acc = x
    # alice turn
    if turns % 2 == 0:
        yield "Bob"
    else:
        yield "Alice"
        


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

test()