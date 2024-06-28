import sys
from collections import deque, defaultdict
import math

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

MOD = 998244353
p2 = [0] * 400001
p2[0] = 1
for i in range(1, 400001):
    p2[i] = (2 * p2[i - 1]) % MOD

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()

    # find min
    s = 1 if a[0] >= 0 else 0
    sm = a[0]
    mn = a[0]
    all_mn_idx = deque([(0, s, sm)])

    for i in range(1, n):
        x = a[i]
        sm = sm + x

        if sm >= 0:
            s += 1
       
        if sm <= mn:
            all_mn_idx.append((i, s, sm))

        if sm < mn:
            mn = sm
 
        
    if mn >= 0:
        yield p2[n] % 998244353
        return
        
    tot = 0
    mn = all_mn_idx[-1][2]
    while len(all_mn_idx) > 0 and all_mn_idx[-1][2] == mn:
        mn_idx, mn_s, _ = all_mn_idx.pop()
        amt = mn_s + n - mn_idx
        if mn < 0:
            amt -= 1
        tot += p2[amt] % MOD
    
    yield tot % MOD
        
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