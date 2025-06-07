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
N = int(2e5) + 5

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

facts = [1]
for i in range(1, N):
    facts.append((facts[-1] * i) % MOD)


def pw(a, b):
    r = 1
    while b > 0:
        if b & 1:
            r = (r * a) % MOD
        b //= 2
        a = (a * a) % MOD
    return r


def mod_inverse(a):
    return pw(a, MOD - 2)

def comb(n, k):
    if n < k:
        return 0
    global facts
    return (facts[n] * pw((facts[n - k] * facts[k]) % MOD, MOD - 2)) % MOD


# use yield to give ans. return to stop
def solve():
    n, k = inlt()
    a = inlt()
    zeros = 0
    ones = 0
    for x in a:
        if x == 0:
            zeros += 1
        else:
            ones += 1
    res = 0
    for amt in range((k + 1) // 2, k + 1):
        if ones < amt:
            break
        res = (res + (((comb(ones, amt) % MOD) * (comb(zeros, k - amt) % MOD)) % MOD)) % MOD
    yield res

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