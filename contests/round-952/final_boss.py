import sys
from collections import deque, defaultdict
import heapq

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
    h, n = inlt()
    heap = []
    init_attack = 0
    d = {}
    a = inlt()
    c = inlt()
    for i in range(n):
        d[a[i]] = c[i]
        init_attack += a[i]
        heapq.heappush(heap, (c[i], a[i]))

    prev_dmg = init_attack
    steps = 1
    while prev_dmg <= h:
        c, a = heapq.heappop(heap)
        steps = c
        prev_dmg += a
        heapq.heappush(heap, (c + d[a], a))

    yield steps



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