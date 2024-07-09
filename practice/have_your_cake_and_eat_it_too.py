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

def get_prefix_sum(a):
    a_sm = [0]

    for x in a:
        a_sm.append(a_sm[-1] + x)


    return a_sm


def binary_search(arr, l, h, x):
    m = 0
 
    while l < h:
        m = (h + l) // 2
        
        if (arr[m] == x):
            return (True, m)
 
        if arr[m] < x:
            l = m + 1
        else:
            h = m

    if arr[m] < x and m < len(arr):
        m += 1
            
    return (False, m)

# use yield to give ans. return to stop
def solve():
    n = inp()
    ps = [get_prefix_sum(inlt()), get_prefix_sum(inlt()), get_prefix_sum(inlt())]

    perms = list(permutations([0, 1, 2]))

    req = ps[0][n] // 3 
    req += 1 if ps[0][n] % 3 != 0 else 0

    for perm in perms:
        a, b, c = perm
        _, ai = binary_search(ps[a], 0, n + 1, req)
        _, bi = binary_search(ps[b], ai + 1, n + 1, req + ps[b][ai])

        if bi >= n:
            continue
        
        a_sm = ps[a][ai]
        b_sm = ps[b][bi] - ps[b][ai]
        c_sm = ps[c][-1] - ps[c][bi]

        if bi >= n:
            continue
        
        if a_sm >= req and b_sm >= req and c_sm >= req:
            s  = [(a, f"1 {ai} "), (b, f"{ai + 1} {bi} "), (c, f"{bi + 1} {n} ")]
            s.sort(key=lambda x: x[0])

            res = ""
            for _, sr in s:
                res += sr
            yield res[:-1]
            return
    
    yield -1
    return 

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