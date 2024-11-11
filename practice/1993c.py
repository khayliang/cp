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
    n, k = inlt()
    a = inlt()
    amax = max(a)
    amod = [x % (2*k) for x in a]
    amodforward = [(x + k - 1) % (2*k) for x in amod]
    intervals = deque([(0, 2 * k - 1)])
    for i in range(n):
        valids = []
        if amod[i] > amodforward[i]:
            valids = [(0, amodforward[i]), (amod[i], 2 * k - 1)]
        else:
            valids = [(amod[i], amodforward[i])]

        amt = len(intervals)
        if amt == 0:
            yield -1
            return
        for _ in range(amt):
            l, r = intervals.pop()
            for x, y in valids:
                if l > y or x > r:
                    continue
                
                intervals.appendleft((max(l, x), min(r, y)))
    
    if not intervals:
        yield -1
        return

    l, _ = intervals[0]
    # value larger than amax that mod is l
    v = (amax // (2*k)) * (2*k) + l
    if v < amax:
        v += 2 * k
    yield v


    
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


test()