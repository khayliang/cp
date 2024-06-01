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
    n = inp()

    prev = 1

    for i in range(1, n):
        k = i + 1
        prev = prev + (2*k - 1) * k
    print(str(prev) + " " + str(2*n - 1))

    ch_arr = [str(i) for i in range(1, n + 1)]
    s = ' '.join(ch_arr)
    sr = ' '.join(reversed(ch_arr))
    print("1 1 " + s,end="")
    
    print("")
    for i in range(2, n + 1):
        print("1 " + str(i) + " " + s)
        print("2 " + str(n - i + 1) + " " + sr)