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
    n, k = inlt()
    a = inlt()
    a.sort(reverse=True)

    lst = a[-1]
    cnt = 1
    a.pop()
    while a and lst == a[-1]:
        a.pop()
        cnt += 1

    while a:
        delta = a[-1] - lst
        if k < delta * cnt:
            break
        k -= delta * cnt
        lst = a[-1]
        while a and lst == a[-1]:
            a.pop()
            cnt += 1
    lst += k // cnt
    k %= cnt
    cnt -= k
    yield (lst * n - cnt + 1)

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