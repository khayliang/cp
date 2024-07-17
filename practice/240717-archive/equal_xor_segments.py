import sys
from collections import deque, defaultdict
from itertools import permutations
from bisect import bisect_left, bisect_right

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
    n, q = inlt()
    a = inlt()

    xors = [0 for _ in range(n + 1)]
    d = defaultdict(lambda: [])

    for i in range(n):
        xors[i + 1] = xors[i] ^ a[i]

    for i in range(n + 1):
        d[xors[i]].append(i)

    for _ in range(q):
        l, r = inlt()
        res = xors[r] ^ xors[l - 1]
        
        if res == 0:
            yield "YES"
            continue
        
        t = d[xors[l - 1]][bisect_right(d[xors[l - 1]], r) - 1]
        s = d[xors[r]][bisect_left(d[xors[r]], l)]
        if t > s:
            yield "YES"
            continue
        yield "NO"
                    
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