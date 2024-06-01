import sys
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

for _ in range(inp()):
    (m, x) = inlt()
    c_arr = []
    h_arr = []
    for i in range(m):
        (c, h) = inlt()
        c_arr.append(c)
        h_arr.append(h)
        
    dp = [float('inf') for _ in range(sum(h_arr) + 1)]
    dp[0] = 0

    mx = 0

    for i in range(m):
        for h in range(sum(h_arr), -1, -1):
            c = dp[h]
            if c + c_arr[i] <= x * i:
                dp[h_arr[i] + h] = min(c + c_arr[i], dp[h_arr[i] + h])
                mx = max(h_arr[i] + h, mx)
    print(mx)

