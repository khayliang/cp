import sys

INF = 10**18

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for i in range(n):
            for j in range(k + 1):
                mn = INF
                for d in range(min(k - j + 1, n - i)):
                    mn = min(mn, a[i + d])
                    dp[i + d + 1][j + d] = min(dp[i + d + 1][j + d], dp[i][j] + (d + 1) * mn)
        
        print(min(dp[n]))

if __name__ == "__main__":
    main()