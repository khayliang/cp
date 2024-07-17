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

def count_inversions(a):
    n = len(a)
    if n == 1:
        return a, 0

    la, li = count_inversions(a[:n // 2])
    ra, ri = count_inversions(a[n // 2:])
    m = n // 2
    l = 0
    r = 0
    s = []
    inv = li + ri
    while l != len(la) or r != len(ra):
        if l == len(la):
            s += ra[r:]
            break
        
        if r == len(ra):
            s += la[l:]
            break
        
        if la[l] < ra[r]:
            s.append(la[l])
            l += 1
        else:
            s.append(ra[r])
            r += 1
            inv += m - l

    return s, inv
        

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()
    b = inlt()

    a_set = set()
    for x in a:
        a_set.add(str(x))
    diff = False
    for i, x in enumerate(b):
        if str(x) not in a_set:
            yield "NO"
            return
        if a[i] != b[i]:
            diff = True

    if not diff:
        yield "YES"
        return

    asorted, ai = count_inversions(a)
    bsorted, bi = count_inversions(b)

    if ai % 2 == bi % 2:
        yield "YES"
    else:
        yield "NO"
    
    

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