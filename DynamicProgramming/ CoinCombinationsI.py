from collections import Counter

MOD = 10**9 + 7

def main():
    n, x = map(int, input().split())
    coins = list(map(int, input().split()))
    dp = Counter()

    dp[0] = 1

    for i in range(1,x+1):
        for coin in coins:
            dp[i] += dp[i-coin]
            dp[i] = dp[i]%MOD
    print(dp[x])

main()