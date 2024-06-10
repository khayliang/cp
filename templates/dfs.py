from collections import deque

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

def dfs(adj_list, x):
    visited = [False for _ in range(len(adj_list))]
    path = []
    curr = x
    visited[x] = True 
    s = deque([x])

    while s:
        curr = s.pop()
        path.append(x)
        for n in adj_list[curr]:
            if not visited[n]:
                s.append((n)
                visited[n] = True
            
    return path
