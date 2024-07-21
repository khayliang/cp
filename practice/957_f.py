import sys
import math
from collections import deque, defaultdict
from itertools import permutations
import bisect
import random

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
    n, x = inlt()
    a  = inlt()

    segments = 1
    exists = defaultdict(lambda: False)
    l = 0
    for r, v in enumerate(a):
        if v > x or x % v != 0:
            continue

        req = x // v

        if exists[req]:
            segments += 1
            l = r
            exists.clear()
            exists[v] = True 
            continue
        del exists[req]
        
        toadd = []
        for factor in exists.keys():
            no = factor * v
            if no < x:
                toadd.append(no)
        for i in toadd:
            exists[i] = True
        exists[v] = True
    
    yield segments

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