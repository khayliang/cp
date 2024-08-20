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
    m = inp()
    for _ in range(m):
        no_d = {} # no points to alpha
        alph_d = {} # alpha points to no
        s = insr()
        if len(s) != n:
            yield "NO"
            continue

        failed = False
        for i, x in enumerate(s):
            curr_no = a[i]
            if x in alph_d and curr_no in no_d and alph_d[x] == curr_no and no_d[curr_no] == x:
                continue
            else:
                if x not in alph_d and curr_no not in no_d:
                    no_d[curr_no] = x
                    alph_d[x] = curr_no
                    continue
                else:
                    yield "NO"
                    failed = True
                    break
        if not failed:
            yield "YES"
        else:
            continue

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