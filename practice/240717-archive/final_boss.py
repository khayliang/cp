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
    a = inlt()
    c = inlt()

    heap = [(0, i) for i in range(n)]
    latest = 0
    while h > 0:
        cooldown, i = heapq.heappop(heap)
        latest = cooldown
        h -= a[i]
        cooldown += c[i]
        heapq.heappush(heap, (cooldown, i))
    
    yield latest + 1

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