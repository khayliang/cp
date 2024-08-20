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
    d = defaultdict(lambda: -1)
    for i, x in enumerate(a):
        d[x] = i

    indexes = sorted(list(d.items()), key=lambda x: x[1])
    k = len(d.keys())

    res = []
    contains = set()
    amt = 0
    curr = 0
    for i in range(len(indexes)):
        val, idx = indexes[i]
        cut = deque(sorted(a[curr : idx]))
        while len(cut) > 0:
            added = False
            # big
            if amt % 2 == 0 and cut[-1] >= val:
                x = cut.pop()
                if x not in contains:
                    res.append(x)
                    contains.add(x)
                    amt += 1
                    added = True
            elif amt % 2 != 0 and cut[0] <= val:
                x = cut.popleft()
                if x not in contains:
                    res.append(x)

                    contains.add(x)
                    amt += 1
                    added = True

            if not added:
                break
        
        if val not in contains:
            res.append(val)
            amt += 1
        curr = idx + 1
    yield k
    yield outlt(res)

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