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
    
MOD = 998244353

def add(x, y):
    x += y
    if x >= MOD:
        x -= MOD
    return x

def mul(x, y):
    return x * y % MOD

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()

    s = sum(a)
    dp = [0] * (s + 1)
    dp[0] = 1
    
    for i in range(n):
        for j in range(s - a[i], -1, -1):
            dp[j + a[i]] = add(dp[j + a[i]], dp[j])
    
    ans = 0
    for j in range(s + 1):
        ans = add(ans, mul((j + 1) // 2, dp[j]))
    
    for i in range(n):
        for j in range(a[i]):
            ans = add(ans, mul(a[i] - (a[i] + j + 1) // 2, dp[j]))
    
    print(ans)



solve()