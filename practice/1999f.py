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
MOD = int(1e9) + 7
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

fact = [1]
for i in range(1, MOD + 5):
    fact.append((fact[-1] * i % MOD) % MOD)

def comb(n, k):
    if n < k:
        return 0
    return fact[n] // (fact[k] * fact[n - k])

def mod_inverse(x):
    x**()

# use yield to give ans. return to stop
def solve():
    n, k = inlt()
    a = inlt()

    ones = 0
    zeros = 0
    for x in a:
        if x == 1:
            ones += 1
        else:
            zeros += 1
            

    left = k // 2

    res = 0
    for i in range(left + 1):
        res = (res % MOD + ((comb(zeros, i) % MOD) * (comb(ones, k - i) % MOD)) % MOD) % MOD
    yield res


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