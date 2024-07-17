import sys
from collections import deque, defaultdict

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

    d = defaultdict(lambda: ([], [0, 0, 0, 0]))
    for i, x in enumerate(a):
        v = x >> 2
        k = x & 3
        d[str(v)][0].append(i)
        d[str(v)][1][k] += 1
    
    for key in d:
        l, amt = d[key]

        l.sort()
        i = 0
        key = int(key)
        for k, x in enumerate(amt):
            no = (key << 2) + k
            for j in range(x):
                a[l[i]] = no
                i += 1
    
    yield outlt(a)
                    
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