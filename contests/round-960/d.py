import sys
import math
from collections import deque, defaultdict
from itertools import permutations
import bisect

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

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()

    steps = 0
    # nth, left, right, both, row
    dp = [INF, INF, INF, INF, 0]
    for x in a:                
        if x == 0:
            dp = [INF, INF, INF, INF, min(dp)]
            continue

        if x > 4:
            dp = [INF, INF, INF, INF, min(dp) + 1]
            continue

        
        ndp = list(dp)
        mn = min(dp)
        if x <= 2:
            if dp[1] != INF or dp[3] != INF:
                ndp[0] = min(dp[1], dp[3])

            ndp[1] = mn + 1
            ndp[2] = INF
            ndp[3] = mn + 2
            ndp[4] = mn + 1
        else:
            if dp[3] != INF:
                ndp[0] = dp[3]
            ndp[4] = mn + 1

            ndp[1] = dp[2] + 1 if dp[2] != INF else INF
            ndp[2] = dp[1] + 1 if dp[1] != INF else INF
            ndp[3] = mn + 2
        dp = ndp
         
    yield min(dp)

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