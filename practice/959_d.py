import sys
import math
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

############ ---- Constants ---- ############
INF = float('inf')


# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()

    parents = [i for i in range(n)]
    sizes = [1 for i in range(n)]

    def find(v):
        curr = v
        pth = deque([v])
        while parents[curr] != curr:
            curr = parents[curr]
            pth.append(curr)
        while pth:
            x = pth.pop()
            parents[x] = curr
        return curr
    
    def union(u, v):
        ru = find(u)
        rv = find(v)

        if ru == rv:
            return
        
        # ru should be the big one, rv small
        if sizes[ru] < rv:
            ru, rv = rv, ru
        
        parents[rv] = ru
        sizes[ru] += sizes[rv]

    res = []

    for i in reversed(range(1, n)):
        rems = [None for _ in range(i)]
        for j, x in enumerate(a):
            r = x % i
            if not rems[r]:
                rems[r] = (j + 1, find(j))
            else:
                if find(j) != rems[r][1]:
                    res.append((j + 1, rems[r][0]))
                    union(j, rems[r][1])
                    break

    yield "Yes"
    for r in reversed(res):
        yield outlt(r)

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