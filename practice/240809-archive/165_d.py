import sys
import math
import heapq
from collections import deque, defaultdict
from itertools import permutations
import bisect
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
    b = inlt()

    order = sorted(range(n), key=lambda i: b[i], reverse=True)
    
    f, p = 0, sum(max(0, b[i] - a[i]) for i in range(n))
    ans = 0
    s = []
    
    if len(s) == k:
        ans = max(ans, p - f)
    
    for i in order:
        p -= max(0, b[i] - a[i])
        heapq.heappush(s, -a[i])
        f += a[i]
        if len(s) > k:
            f -= -heapq.heappop(s)
            
        if len(s) == k:
            ans = max(ans, p - f)

    yield ans



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