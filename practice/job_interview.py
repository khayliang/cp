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

############ ---- Output Parsing Functions ---- ############
def outlt(a):
    return " ".join(map(str, a))

# use yield to give ans. return to stop
def solve():
    n, m = inlt()
    a = inlt()
    b = inlt()
    joined = list(zip(a, b))

    N = n + m + 1

    score = 0
    suboptimal = -1
    prog_count = 0
    test_count = 0
    typ = []

    for i in range(N - 1):
        if prog_count == n:
            if a[i] > b[i] and suboptimal == -1:
                suboptimal = i
            score += b[i]
            test_count += 1
            typ.append(1)
            continue
        elif test_count == m:
            if a[i] < b[i] and suboptimal == -1:
                suboptimal = i
            score += a[i]
            prog_count += 1
            typ.append(0)
            continue
        
        if a[i] > b[i]:
            score += a[i]
            prog_count += 1
            typ.append(0)
        else:
            score += b[i]
            test_count += 1
            typ.append(1)

    score += joined[N - 1][typ[suboptimal]]

    res = []
    for i in range(N - 1):
        curr = score
        if i < suboptimal or suboptimal == -1:
            if typ[i] != typ[suboptimal]:
                curr -= joined[i][typ[i]]
                curr -= joined[suboptimal][typ[suboptimal]]
                curr += joined[suboptimal][typ[i]]
            else:
                curr -= joined[i][typ[i]]
        else:
            curr -= joined[i][typ[i]]
        res.append(curr)
    res.append(score - joined[N - 1][typ[suboptimal]])

    yield outlt(res)

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