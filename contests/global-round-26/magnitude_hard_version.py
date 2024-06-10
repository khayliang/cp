import sys
from collections import deque, defaultdict

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

CONST = 998244353

# use yield to give ans. return to stop
def solve():
    n = inp()
    a = inlt()

    mn_arr = [0] * n
    mx_arr = [0] * n
    mn_count = [0] * n
    mx_count = [0] * n
    for i, x in enumerate(a):
        if x == 0:
            continue

        prev_mn = mn_arr[i - 1] if i > 0 else 0
        prev_mx = mx_arr[i - 1] if i > 0 else 0

        nos = [prev_mn + x, abs(prev_mn + x), prev_mx + x, abs(prev_mx + x)]

        mn_arr[i] = min(nos)
        mx_arr[i] = max(nos)

        for y in nos:
            if y == mn_arr[i]:
                mn_count[i] += 1
            elif y == mx_arr[i]:
                mx_count[i] += 1
        
    k = max(abs(mn_arr[-1]), abs(mx_arr[-1]))
    print("min: ", mn_arr)
    print("max: ", mx_arr)
    print("min count: ", mn_count)
    print("max count: ", mx_count)

    q = deque([])
    if mn_arr[-1] == -k and mx_arr[-1] == -k:
        q.append((-k, n - 1, 2))
    elif mn_arr[-1] == -k or mx_arr[-1] == -k:
        q.append((-k, n - 1, 1))

    if mn_arr[-1] == k and mx_arr[-1] == k:
        q.append((k, n - 1, 2))
    elif mn_arr[-1] == k or mx_arr[-1] == k:
        q.append((k, n - 1, 1))

    for i in range(n - 1, 0, -1):
        print(q)
        nos = {}
        while q and q[0][1] == i:
            c, _, count = q.popleft()
            nos[c] = count
        
        for c in nos:
            count = nos[c]
            print("c: ", c)
            opt1 = c - a[i]
            opt2 = - c - a[i]
            print("opt1, opt2: ", opt1, opt2)

            # opt 1
            prev_count = count
            count = 0
            if opt1 == mn_arr[i - 1]:
                count += prev_count * mn_count[i - 1]
            if opt1 == mx_arr[i - 1]:
                count += prev_count * mx_count[i - 1]
            if opt1 == mn_arr[i - 1] or opt1 == mx_arr[i - 1]:
                q.append((opt1, i, count))    

            # opt 2
            count = 0
            if opt2 == mn_arr[i - 1]:
                count += prev_count * mn_count[i - 1]
            if opt2 == mx_arr[i - 1]:
                count += prev_count * mx_count[i - 1]
            if opt2 == mn_arr[i - 1] or opt2 == mx_arr[i - 1]:
                q.append((opt2, i, count))
    count = 0
    for _, _, c in q:
        count += c
    yield count
            
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