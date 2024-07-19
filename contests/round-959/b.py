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
    s = insr()
    t = insr()
    t1 = -1
    s1 = -1
    for i in range(n):
        if s[i] == "1":
            yield "YES"
            return
        if t[i] == "1" and s[i] == "1":
            yield "YES"
            return
        if t[i] == "1" and s[i] == "0":
            yield "NO"
            return
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