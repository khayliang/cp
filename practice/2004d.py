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
    n, q = inlt()
    a = input().split()
    portals = defaultdict(lambda: [])
    for i, x in enumerate(a):
        portals[x].append(i)
    for _ in range(q):
        x, y = inlt()
        px = a[x - 1]
        py = a[y - 1]
        xcolors = set(px)
        ycolors = set(py)

        meds = []
        found = False
        for c in xcolors:
            if c in ycolors:
                yield abs(y - x)
                found = True
                break
            for d in ycolors:
                meds.append("".join(sorted([c, d])))
        if found:
            continue

        mn = INF
        for p in meds:
            m = len(portals[p])
            if m == 0:
                continue
            l = bisect.bisect_left(portals[p], x - 1)
            r = bisect.bisect_left(portals[p], y - 1)
            # lleft
            ll = portals[p][max(0, l - 1)] + 1
            mn = min(mn, abs(ll - x) + abs(ll - y))
            # lright
            lr = portals[p][min(m - 1, l)] + 1
            mn = min(mn, abs(lr - x) + abs(lr - y))
            # rleft
            rl = portals[p][max(0, r - 1)] + 1
            mn = min(mn, abs(rl - x) + abs(rl - y))
            # rright
            rr = portals[p][min(m - 1, r)] + 1
            mn = min(mn, abs(rr - y) + abs(rr - x))
        
        if mn == INF:
            yield -1
        else:
            yield mn

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