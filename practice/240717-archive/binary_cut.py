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
    start = None
    zeros = []
    for i, x in enumerate(s):
        if x == "0":
            if start == None:
                start = i
        else:
            if start != None:
                zeros.append((start, i))
                start = None
    if start:
        zeros.append((start, len(s)))

    if not zeros:
        yield 1
        return
    
    if zeros[0][0] == 0 and zeros[0][1] == len(s):
        yield 1
        return

    amt = len(zeros) * 2

    if len(zeros) > 0:
        if zeros[0][0] != 0:
            amt += 1
        if zeros[-1][1] == len(s):
            amt -= 1

        if len(zeros) == 1 and zeros[-1][1] == len(s):
            pass
        else:
            amt -= 1
    if amt == 0:
        amt += 1
    
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