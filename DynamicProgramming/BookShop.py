from collections import defaultdict,Counter


def solver(prices,pages,n,money):
    dp = defaultdict(Counter)
    for i in range(n+1):
        for w in range(money+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            
            elif prices[i-1] <= w :
                dp[i][w] = max (
                    pages[i-1] + dp [i-1][w-prices[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp [i-1][w]
    return dp[n][money]


    


def main():
    n,money = map(int,input().split())
    prices = list(map(int,input().split()))
    pages = list(map(int,input().split()))

    print(solver(prices,pages,n,money))

main()