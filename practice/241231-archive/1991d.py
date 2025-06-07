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

"""
Primes within the range 0 to n
"""
def sieve_of_eratosthenes(n):
    prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    prime_numbers = []
    for p in range(2, n + 1):
        if prime[p]:
            prime_numbers.append(p)
    return prime_numbers

# use yield to give ans. return to stop
def solve():
    n = inp()
    if n == 1:
        yield 1
        yield outlt([1])
    elif n == 2:
        yield 2
        yield outlt([1, 2])
    elif n == 3:
        yield 2
        yield outlt([1, 2, 2])
    elif n == 4:
        yield 3
        yield outlt([1, 2, 2, 3])
    elif n == 5:
        yield 3
        yield outlt([1, 2, 2, 3, 3])
    elif n == 6:
        yield 4
        yield outlt([1, 2, 2, 3, 3, 4])
    else:
        yield 4
        res = []
        for i in range(1, n+1):
            res.append(i % 4 + 1)
        yield outlt(res)
    
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