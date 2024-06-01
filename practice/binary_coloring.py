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
    x = inp()
    b = list(reversed(bin(x)[2:]))
    for i in range(len(b) - 1):
        if b[i] != "0" and b[i + 1] != "0":
            b[i] = "-1"
            b[i + 1] = "0"
            
            j = i + 2
            while j < len(b) and b[j] != "0":
                b[j] = "0"
                j += 1
            
            
            if j == len(b):
                b.append("1")
            else:
                b[j] = "1"
    print(len(b))
    print(*b)