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
def outlt(ac):
    return " ".join(map(str, ac))

############ ---- Constants ---- ############
INF = float('inf')

############ ---- Function to Bootstrap Recursion ---- ############
"""
Add the decorator @bootstrap above the recursive function.
For the recursion to work, yield the recusive function.
Recursive function must yield something regardless
To return ac value, add the line yield yield fn()
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
    n, m = inlt()
    ac = list(zip(inlt(), inlt()))
    ac.sort(key=lambda x: x[0])

    res = 0
    for i in range(n):
        if i + 1 < n and ac[i + 1][0] == ac[i][0] + 1:
            k1 = min(ac[i][1], m // ac[i][0])
            coins = m - k1 * ac[i][0]
            k2 = min(ac[i + 1][1], coins // ac[i + 1][0])
            coins -= k2 * ac[i + 1][0]

            r = min(ac[i + 1][1] - k2, coins, k1)

            res = max(res, (k1 - r) * ac[i][0] + (k2 + r) * ac[i + 1][0])

        res = max(res, min((m // ac[i][0]), ac[i][1]) * ac[i][0])
    
    yield res
        
def test():
    ans = []
    for _ in range(inp()):
        for ac in solve():
            ans.append(ac)
    for i in ans:
        print(i)

def submit():
    for _ in range(inp()):
        for ac in solve():
            print(ac)

submit()