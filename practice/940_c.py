import sys
import math
from collections import deque, defaultdict
from itertools import permutations
import bisect

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

MOD = int(1e9) + 7

# use yield to give ans. return to stop
def solve():
    n, k = inlt()
    avail = set(i + 1 for i in range(n))
    for _ in range(k):
        r, c = inlt()
        if r == c:
            avail.remove(r)
        else:
            avail.remove(r)
            avail.remove(c)
    avail = list(avail)
    amt = len(avail)
    dp = [1, 1]
    for i in range(2, amt + 1):
        dp.append((dp[-1] + 2 * (i - 1) * dp[-2] % MOD) % MOD) 
    yield dp[-1]

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