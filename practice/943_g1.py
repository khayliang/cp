import sys
import math
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

def z_function(s):
    n = len(s)
    z = [0 for _ in range(n)]
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z
    

# use yield to give ans. return to stop
def solve():
    n, k, _ = inlt()
    s = insr()

    z = z_function(s)

    if k == 1:
        yield n
        return
    
    @bootstrap
    def find(l=0, r=n):
        if l >= r - 1:
            yield l
        m = (l + r) // 2
        amt = 1
        i = m
        while i < n:
            if z[i] >= m:
                amt += 1
                i += m
            else:
                i += 1

        if amt < k:
            yield (yield find(l, m))
        else:
            yield (yield find(m, r))
    
    yield find()
        
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