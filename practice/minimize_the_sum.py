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
    [n, k] = inlt()
    arr = inlt()

    if n <= 1:
        print(sum(arr))
        continue

    for _ in range(k):
        max_diff = -1
        min_no = float('inf')
        best_idx = 0
        for i in range(n - 1):
            diff = abs(arr[i] - arr[i + 1])
            if diff > max_diff:
                max_diff = diff
                min_no = min(arr[i], arr[i + 1])
                best_idx = i
                continue
            if diff == max_diff:
                curr_min = min(arr[i], arr[i + 1])
                if curr_min < min_no:
                    min_no = curr_min
                    best_idx = i
        
        arr[best_idx] = min_no
        arr[best_idx + 1] = min_no

    print(arr)
    print(sum(arr))