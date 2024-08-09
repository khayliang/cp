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

Z = 30
MAX_N = 10**5 + 3
pref = [[[0 for _ in range(2)] for _ in range(MAX_N)] for _ in range(Z)]
suff = [[[0 for _ in range(2)] for _ in range(MAX_N)] for _ in range(Z)]

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = [0] + inlt()

    for i in range(Z):
        suff[i][n+1][0] = suff[i][n+1][1] = 0
    
    for i in range(Z):
        for j in range(1, n+1):
            t = int(bool(a[j] & (1 << i)))
            for k in range(2):
                pref[i][j][k] = (t == k) + pref[i][j-1][k ^ t]
        
        for j in range(n, 0, -1):
            t = int(bool(a[j] & (1 << i)))
            for k in range(2):
                suff[i][j][k] = (t == k) + suff[i][j+1][k ^ t]
    
    ans = 0
    for i in range(1, n+1):
        z = a[i].bit_length() - 1
        ans += pref[z][i-1][1] * (1 + suff[z][i+1][0])
        ans += (1 + pref[z][i-1][0]) * suff[z][i+1][1]
    
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