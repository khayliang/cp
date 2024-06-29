# https://usaco.guide/silver/more-prefix-sums?lang=py

def prefix_sum(n, m, matrix):
    res = [[0 for j in range(m)] for i in range(n)]
    res[0][0] = matrix[0][0]
    for i in range(1, n):
        res[i][0] = res[i - 1][0] + matrix[i][0]
    for i in range(1, m):
        res[0][i] = res[0][i - 1] + matrix[0][i]
    
    for i in range(1, n):
        for j in range(1, m):
            res[i][j] = res[i - 1][j] + res[i][j - 1] - res[i - 1][j - 1] + matrix[i][j]

    return res

"""
a: start row index
b: start col index
A: end row index
B: end col index
"""
def query(mat, a, b, A, B):
    sm = mat[A][B]
    if a > 0:
        sm -= mat[a - 1][B]
    if b > 0:
        sm -= mat[A][b - 1]
    if x > 0 and y > 0:
        sm += mat[a - 1][b - 1]