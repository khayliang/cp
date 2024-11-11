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

letters = set(list("narek"))
letters_list = list("narek")
    
# use yield to give ans. return to stop
def solve():
    n, m = inlt()
    # represents the maximum score suppose we're looking for the ith character in narek
    dp = [-INF for _ in range(5)]
    dp[0] = 0
    for _ in range(n):
        ndp = list(dp)
        w = insr()
        for i in range(5):
            if dp[i] == -INF:
                continue
            curr_i = i
            score = 0
            for c in w:
                if c not in letters:
                    continue
                score -= 1
                if c == letters_list[curr_i]:
                    curr_i += 1
                    if curr_i % 5 == 0:
                        score += 10
                        curr_i = 0
            ndp[curr_i] = max(ndp[curr_i], dp[i] + score)

        dp = ndp
    yield max(dp) if max(dp) != -INF else 0
    
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