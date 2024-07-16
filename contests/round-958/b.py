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
    a = insr()
    zeros = 0
    ones = 0
    for i, x in enumerate(a):
        if x == "0":
            if i == 0:
                zeros += 1
            elif a[i - 1] == "1":
                zeros += 1
        else:
            ones += 1
    if ones > zeros:
        yield "Yes"
    else:
        yield "No"
    
            


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