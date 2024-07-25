from types import GeneratorType

# Note: the bootstrapped function needs to yield something regardless
def bootstrap(f, stack=[]):
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
    
"""
Given an undirected graph, we want to find all edges such that when an edge is removed, 
the number of components will increase by one.

adj: adj list indexed by 0
returns: a list of tuples representing bridge edges
"""
def find_bridges(adj):
    n = len(adj)
    t = [float('inf') for _ in range(n)]
    earliest = [float('inf') for _ in range(n)]
    index = [0]
    bridges = []

    @bootstrap
    def dfs(adj, curr=0, parent=0, index=index, t=t, earliest=earliest, bridges=bridges):
        ind = index[0]
        t[curr] = ind

        if len(adj[curr]) == 0:
            earliest[curr] = ind
            yield
        
        for c in adj[curr]:
            if c == parent:
                continue

            if t[c] < float('inf'):
                earliest[curr] = min(earliest[curr], t[c])
                continue

            index[0] += 1
            yield dfs(adj, c, curr, index, t, earliest, bridges)
            earliest[curr] = min(earliest[curr], earliest[c])
            if t[curr] < earliest[c]:
                bridges.append((curr, c))
            
        yield

    dfs(adj)

    return bridges

if __name__ == "__main__":
    adj_list = [[1, 2], [0, 2], [0, 1, 3], [2, 4, 5], [3, 5], [3, 4]]
    print(find_bridges(adj_list))