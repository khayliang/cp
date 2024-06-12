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
    n = inp()
    a = inlt()

    heap = []
    prev_sum = 0
    good = 0
    for i in range(n):
        good_curr = False
        if a[i] == prev_sum:
            good_curr = True

        if a[i] >= prev_sum:
            heapq.heappush(heap, a[i])

        curr_sum = prev_sum + a[i]
        to_pop = 0
        for j in heap:
            if len(heap) == 0:
                break
            if j < curr_sum - j:
                to_pop += 1
                continue

            if j == curr_sum - j:
                good_curr = True
                continue

            elif j > curr_sum - j:
                break
        
        for i in range(to_pop):
            heapq.heappop(heap)

        if good_curr:
            good += 1
            
        prev_sum = curr_sum

    yield good
        
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