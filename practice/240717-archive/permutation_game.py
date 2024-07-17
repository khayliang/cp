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
    n, k, pb, ps = inlt()
    pb_init = pb
    ps_init = ps
    p = [0] + inlt()
    a = [0] + inlt()

    bmx = 0
    smx = 0
    bsm = 0
    ssm = 0
    for i in range(1, min(k + 1, n + 1)):
        bsm += a[pb]
        ssm += a[ps]

        bmx = max(bmx, bsm + (k - i) * a[pb])
        smx = max(smx, ssm + (k - i) * a[ps])

        pb = p[pb]
        ps = p[ps]

    if bmx > smx:
        yield "Bodya"
    elif bmx == smx:
        yield "Draw"
    else:
        yield "Sasha"
    
    


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