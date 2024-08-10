import sys
import math
import heapq
import bisect
from collections import deque, defaultdict
from itertools import permutations
from types import GeneratorType

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

############ ---- Function to Bootstrap Recursion ---- ############
"""
Add the decorator @bootstrap above the recursive function.
For the recursion to work, yield the recusive function.
Recursive function must yield something regardless
To return a value, add the line yield yield fn()
"""
def bootstrap(f, stack=deque()):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def tangent(disk1, disk2):
    sq_dist = (disk1[0] - disk2[0]) ** 2 + (disk1[1] - disk2[1]) ** 2
    return ((disk1[2] + disk2[2]) ** 2) == sq_dist

# use yield to give ans. return to stop
def solve():
    # find if an open trail exists with length > 3. 
    # If trail exists then return True, else return False

    # two disks are connected if their distance between centers are
    # obtainable by adding their radius together

    n = inp()
    disks = []
    for _ in range(n):
        disks.append(inlt())
    
    adj = [[] for _ in range(n)]
    for i, parent in enumerate(disks):
        for j, child in enumerate(disks):
            if parent == child:
                continue
            if tangent(parent, child):
                adj[i].append(j)
    coloring = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    stk = deque()
    for i in range(n):
        whites = 0
        blacks = 0
        bipartite = True
        if not visited[i]:
            stk.append((i, i))
            visited[i] = True
        while stk:
            parent, curr = stk.pop()
            adj_colors = set()
            for child in adj[curr]:
                if not visited[child]:
                    visited[child] = True
                    stk.append((curr, child))
                    continue
                adj_colors.add(coloring[child])
                
            if 0 not in adj_colors:
                coloring[curr] = 0
            elif 1 not in adj_colors:
                coloring[curr] = 1
            else:
                coloring[curr] = 2

            if coloring[curr] > 1:
                bipartite = False
            else:
                if coloring[curr] == 1:
                    blacks += 1
                else:
                    whites += 1
        if bipartite and whites != blacks:
            print("YES")
            return
    
    print("NO")

solve()
    
    
