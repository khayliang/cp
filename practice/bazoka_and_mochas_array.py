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
    arr = inlt()
    subseq_min = arr[0]
    v = False
    failed = False
    for i in range(1, len(arr)):
        if v and arr[i] > subseq_min:
            failed = True
            break
        
        if arr[i] >= arr[i - 1]:
            continue


        if not v:
            v = True
        else:
            failed = True
            break
        
        if arr[i] > subseq_min:
            failed = True
            break
    if failed:
        print("No")
        continue
        
    print("Yes")
        


