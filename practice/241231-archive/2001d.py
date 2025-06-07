import sys
import math
import heapq
import bisect
from collections import deque, defaultdict
from itertools import permutations
from types import GeneratorType

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

############ ---- Function to Bootstrap Recursion ---- ############
"""
Add the decorator @bootstrap above the recursive function.
For the recursion to work, yield the recusive function.
Recursive function must yield something regardless
To return a value, add the line yield yield fn()
"""
def bootstrap(f, stack=deque()):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
    

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()
    d = defaultdict(lambda: 0)
    for i, x in enumerate(a):
        d[x] = i

    res = []

    mnhp = []
    mxhp = []
    l = -1
    r = -1
    added = set()
    for k in sorted(d.values()):
        if len(res) == len(d.keys()):
            break
            
        i = r + 1
        r = k
        while i <= r:
            if a[i] not in added:
                heapq.heappush(mnhp, (a[i], i))
                heapq.heappush(mxhp, (-a[i], i))
            i += 1
        v = a[k]
        if v in added:
            continue

        while True:
            # max
            if len(res) % 2 == 0:
                if not mxhp:
                    break
                w, j = heapq.heappop(mxhp)
                w = -w
                if j <= l or w in added:
                    continue

                while mxhp and w == -mxhp[0][0]:
                    _, ji = heapq.heappop(mxhp)
                    if ji > l:
                        j = min(j, ji)

                if w >= v:
                    res.append(w)
                    added.add(w)
                    l = j
                    if w == v:
                        break
            else:
                if not mnhp:
                    break
                w, j = heapq.heappop(mnhp)
                if j <= l or w in added:
                    continue

                while mnhp and w == mnhp[0][0]:
                    _, ji = heapq.heappop(mnhp)
                    if ji > l:
                        j = min(j, ji)
                    
                if w <= v:
                    res.append(w)
                    added.add(w)
                    l = j
                    if w == v:
                        break

    yield len(res)
    yield outlt(res)
                
def test():
    ans = []
    for _ in range(inp()):
        for a in solve():
            ans.append(a)
    for i in ans:
        print(i)
        sys.stdout.flush()


def submit():
    for _ in range(inp()):
        for a in solve():
            print(a)
            sys.stdout.flush()

submit()