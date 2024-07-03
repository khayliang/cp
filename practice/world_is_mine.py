import sys
from collections import deque, defaultdict

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

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()
    d = defaultdict(lambda: 0)
    for x in a:
        d[x] += 1
    
    a = sorted(d.keys())
    c = [d[x] for x in a]

    m = len(a)

    dp = [float('inf') for _ in range(m + 1)]
    dp[0] = 0
    
    for i in range(1, m + 1):
        ndp = list(dp)
        for j in range(1, m + 1):
            s = dp[j - 1] + c[i - 1]
            if s <= i - j:
                ndp[j] = min(dp[j], s)
        dp = ndp
    
    k = 0
    for i in range(m + 1):
        if dp[i] != float('inf'):
            k = i
    
    yield m - k

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