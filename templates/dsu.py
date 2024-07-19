from collections import deque

parent = [i for i in range(n)]
size = [1 for _ in range(n)]

def find(x):
    curr = x
    pth = deque([x])
    while curr != parent[curr]:
        curr = parent[curr]
        pth.append(curr)
    while pth:
        nd = pth.pop()
        parent[nd] = curr
    return curr

def union(u, v):
    ru = find(u)
    rv = find(v)

    if (ru != rv):
        if size[ru] > size[rv]:
            parent[rv] = ru
            size[ru] += size[rv]
        else:
            parent[ru] = rv
            size[rv] += size[ru]
    
