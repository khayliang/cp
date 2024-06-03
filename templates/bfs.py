from collections import deque

def bfs_shortest_path(adj_list, start, end):
    visited = [False for _ in range(len(adj_list))]
    prev = [None for _ in range(len(adj_list))]
    q = deque([start])

    curr = start
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

            

