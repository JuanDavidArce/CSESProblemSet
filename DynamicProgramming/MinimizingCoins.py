from math import inf

def main():
    n,x = map(int,input().split())
    coins = list(map(int,input().split()))
    dp = [inf for _ in range(x+1)]
    dp[0]= 0

    for i in range(1,x+1):
        for j in range(n):
            if i - coins[j] >= 0 :
                dp[i] = min(dp[i],dp[i-coins[j]]+1)
    if dp[x] != inf:
        print(dp[x])
    else:
        print(-1)
main()