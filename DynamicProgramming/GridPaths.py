from collections import defaultdict,Counter

def main():
    dp = defaultdict(Counter)
    MOD = 10**9 + 7
    n = int(input())
    dp[0][0] = 1
    for i in range(n):
        row = input()
        for j in range(n):
            if row[j]==".":
                if i>0:
                    dp[i][j] += dp[i-1][j]
                    dp[i][j] = dp[i][j]%MOD
                if j>0:
                    dp[i][j] += dp[i][j-1]
                    dp[i][j] = dp[i][j]%MOD
            else: dp[i][j] = 0
    print(dp[n-1][n-1])
main()

