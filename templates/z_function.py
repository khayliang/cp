"""
returns an array where the ith element is equal to the
greatest number of characters starting from position i
"""
def z_function(s):
    n = len(s)
    z = [0 for _ in range(n)]
    l, r = 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z