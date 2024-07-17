import sys
from collections import deque, defaultdict
from itertools import permutations

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
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y = inlt()
        x -= 1
        y -= 1
        adj[x].append(y)
        adj[y].append(x)
    
    tmp = deque([(0, -1)])
    postordering = deque()

    while tmp:
        c, p = tmp.pop()
        postordering.append((c, p))
        for v in adj[c]:
            if v == p:
                continue
            tmp.append((v, c))
    
    dp = [[(INF, INF), (INF, INF)] for _ in range(n)]
    while postordering:
        v, p = postordering.pop()
        steps = [[] for _ in range(len(adj[v]) + 4)]

        tot_dmg = 0
        for c in adj[v]:
            if c == p:
                continue

            dmg, step = dp[c][0]
            tot_dmg += dmg
            steps[step].append(c)
        
        for step in range(1, len(adj[v]) + 2):
            curr_dmg = tot_dmg + a[v] * step
            for c in steps[step]:
                curr_dmg -= dp[c][0][0]
                curr_dmg += dp[c][1][0]
            
            if curr_dmg < dp[v][0][0]:
                dp[v][1] = dp[v][0]
                dp[v][0] = (curr_dmg, step)
            elif curr_dmg < dp[v][1][0]:
                dp[v][1] = (curr_dmg, step)

    yield dp[0][0][0]

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
