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
    s = insr()
    ones = []

    prev = None
    for i, x in enumerate(s):
        if x == "1":
            if prev == None:
                prev = i
        else:
            if prev != None:
                ones.append([prev, i])
                prev = None

    if prev != None:
        ones.append([prev, len(s)])

    if not ones:
        yield 0
        return
    
    pos = ones[0]
    size = pos[1] - pos[0]

    cost = 0
    for i in range(1, len(ones)):
        diff = ones[i][0] - pos[1]
        cost += diff * (size + 1)
        pos[0] += diff
        pos[1] = ones[i][1]
        size = pos[1] - pos[0]
    
    if pos[1] != len(s):
        diff = len(s) - pos[1]
        cost += diff * (size + 1)
    
    yield cost


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