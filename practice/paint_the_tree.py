import sys
from collections import deque

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

def bfs_shortest_path(adj_list, start, end):
    visited = [False for _ in range(len(adj_list))]
    prev = [None for _ in range(len(adj_list))]
    q = deque([])

    curr = start
    q.append(curr)
    visited[curr] = True
    prev[curr] = curr

    while curr != end:
        curr = q.popleft()
        for n in adj_list[curr]:
            if not visited[n]:
                q.append(n)
                visited[n] = True
                prev[n] = curr
                
                if n == end:
                    break
        if visited[end]:
            break
    
    curr = end
    path = [end]
    while curr != start:
        curr = prev[curr]
        path.append(curr)
    return list(reversed(path))

def furthest_distance_from_vertex(adj_list, x):
    visited = [False for _ in range(len(adj_list))]
    curr = (x, 0)
    visited[x] = True 
    s = deque([(x, 0)])

    max_dist = 0

    while s:
        curr, curr_dist = s.pop()
        max_dist = max(max_dist, curr_dist)
        for n in adj_list[curr]:
            if not visited[n]:
                s.append((n, curr_dist + 1))
                visited[n] = True
            
    return max_dist


for _ in range(inp()):
    n = inp()
    a, b = inlt()
    adj = [[] for _ in range(n)]
    parents = [None for _ in range(n)]
    for _ in range(n - 1):
        x, y = inlt()
        adj[x - 1].append(y - 1)
        adj[y - 1].append(x - 1)
        parents[y - 1] = x - 1
    
    path = bfs_shortest_path(adj, a - 1, b - 1)

    steps = len(path) // 2
    meet_at = path[((len(path)) // 2) - 1 if len(path) % 2 == 0 else (len(path) // 2)]

    curr = meet_at
    dist = furthest_distance_from_vertex(adj, curr)
    print((n - 1) * 2 - dist + steps)