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

m, n = inlt()
s = inlt()
l = inlt()

dp = [0 for _ in range(m)]
dp[0] = 1

for _ in range(n):
    ndp = []
    for i in range(m):
        sm = 0
        for j in range(m):
            # s l
            sm += int(dp[j] * s[j] * l[i] % (10e9 + 7))
            # s s
            sm += int(dp[j] * s[j] * s[i] % (10e9 + 7))
            # l s
            sm += int(dp[j] * l[j] * s[i] % (10e9 + 7))
        ndp.append(sm) 
    dp = ndp

print(int(sum(dp) % (10e9 + 7)))