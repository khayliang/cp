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
    n = inp()
    a = inlt()
    b = inlt()
    
    amt = 0
    for i in range(n):
        amt += abs(a[i] - b[i])
        
    closest = float('inf')

    for i in range(n):
        if abs(a[i] - b[-1]) < abs(closest - b[-1]):
            closest = a[i]
        if abs(b[i] - b[-1]) < abs(closest - b[-1]):
            closest = b[i]
        if sorted([a[i], b[-1], b[i]])[1] == b[-1]:
            yield amt + 1
            return 

    amt += 1 + abs(closest - b[-1])
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

submit()