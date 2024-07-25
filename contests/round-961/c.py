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

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()
    amt = 0
    for i in range(1, n):
        if a[i] >= a[i - 1]:
            continue
        
        if a[i] == 1:
            yield -1
            return
        k = math.ceil(math.log(a[i - 1]) / math.log(a[i]))
        x = math.ceil(math.log(k) / math.log(2))
        p = 1 << x
        amt += x
        a[i] = int(math.pow(a[i], p))

    yield amt

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