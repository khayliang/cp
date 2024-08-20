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
    objs = []
    ones = 0
    for _ in range(n):
        a, b = inlt()

        if a == 1 and b == 1:
            ones += 1
            continue
        
        cost = min(a, b)
        total = max(a, b)
        objs.append((total, cost))
    objs.sort(key=lambda x: x[1])

    curr = 0
    steps = 0
    if ones * 2 > k:
        steps = math.ceil(k / 2)
        curr = steps * 2
    else:
        steps = ones
        curr = ones * 2

    for total, cost in objs:
        if curr >= k:
            break
        if curr + total + cost <= k:
            curr += total + cost
            steps += cost * total
        else:
            diff = k - curr
            to_square = total - cost
            if diff <= to_square:
                steps += cost * diff
                curr += diff
            else:
                steps += cost * to_square
                curr += to_square
            square_side = cost
            if cost == 1:
                curr += 2
                steps += 1
                continue
            
            curr += 1
            steps += cost
            cost -= 1
            if curr >= k:
                yield steps
                return
            for i in range(cost * 2):
                steps += cost
                curr += 1
                if curr >= k:
                    yield steps
                    return
                if i % 2 == 1:
                    cost -= 1
                
                




    if curr >= k:
        yield steps
    else:
        yield -1

        

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