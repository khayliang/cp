import sys
import math
from collections import deque, defaultdict
from itertools import permutations
import bisect
import random

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

def correct_solve(n, m, a):
    mx = 0
    sm = 0
    a.sort()
    l = 0
    for r in range(n):

        x = a[r]
        prev = a[l]

        if x > m:
            break
        
        sm += x
        
        if x != prev and x - 1 != prev:
            while a[l] < a[r] - 1:
                sm -= a[l]
                l += 1

        while sm > m and l < r:
            sm -= a[l]
            l += 1

        mx = max(sm, mx)
    return mx
# use yield to give ans. return to stop
def solve(n, m, a, c):

    ac = sorted(list(zip(a, c)), key=lambda x: x[0])

    mx = 0
    for i in range(n):
        if ac[i][0] > m:
            break

        # single value case
        if i == n -1 or ac[i + 1][0] > ac[i][0] + 1:
            x = ac[i][0]
            quot = m // x
            val = min(ac[i][1], quot) * x
            mx = max(val, mx)
            continue
        
        # multi value case
        x = ac[i][0]
        amt = ac[i][1]
        v = m % x
        u = (m // x) - v
        if u > amt:
            val = amt * x
            rest = m - val
            if ac[i + 1][0] <= rest:
                val += min((rest // (x + 1)), ac[i + 1][1]) * (x + 1)
            mx = max(val, mx)
        else:
            val = u * x + min(ac[i + 1][1], v) * (x + 1)
            mx = max(val, mx)
        
        x = ac[i + 1][0]
        amt = ac[i + 1][1]
        v = m % x
        u = (m // x) - v
        if u > amt:
            val = amt * x
            rest = m - val
            if ac[i - 1][0] <= rest:
                val += min((rest // (x - 1)), ac[i][1]) * (x - 1)
            mx = max(val, mx)
        else:
            val = u * x + min(ac[i][1], v) * (x - 1)
            mx = max(val, mx)

    return mx


        

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


while True:
    n = 3
    m = random.randint(1, 10)
    a = [random.randint(1,3)]
    for i in range(n - 1):
        a.append(a[-1] + random.randint(0,3))

    amt = defaultdict(lambda: 0)

    for x in a:
        amt[x] += 1

    l = [(k, v) for k, v in amt.items()]

    res = [[i for i, j in l],
        [j for i, j in l]]
    if correct_solve(n, m, a) != solve(len(l), m, res[0], res[1]):
        print(l, m)
        break
    else:
        print("Correct")
