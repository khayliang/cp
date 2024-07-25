from collections import deque
from types import GeneratorType

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

# returns list of lists, where each list contain the vertices that make up a component
# adj list indexed from 0
def tarjans_algorithm(adj):
    n = len(adj)

    components = []
    indexlist = [float('inf') for _ in range(n)]

    @bootstrap
    def strongconnect(
        v, 
        components,
        idx=0,
        indexlist=indexlist, 
        lowlink=[float('inf') for _ in range(n)],
        onstack=set(),
        S=deque()
    ):
        indexlist[v] = idx
        lowlink[v] = idx
        idx = idx + 1
        S.append(v)
        onstack.add(v)

        for w in adj[v]:
            if indexlist[w] == float('inf'):
                yield strongconnect(w, components, idx, indexlist, lowlink, onstack, S)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in onstack:
                lowlink[v] = min(lowlink[v], indexlist[w])
        
        if lowlink[v] == indexlist[v]:
            comp = []
            while S:
                w = S.pop()
                onstack.remove(w)
                comp.append(w)

                if w == v:
                    break
            components.append(comp)
        yield None
    
    for i in range(n):
        if indexlist[i] == float('inf'):
            strongconnect(i, components, indexlist=indexlist)

    return components

                

if __name__ == "__main__":
    adj_list = [[1, 2], [0, 2], [3], [4, 5], [3, 5], [3]]
    print(tarjans_algorithm(adj_list))

            
        
    
