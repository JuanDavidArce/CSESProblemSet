from math import inf


def main():
    n = int(input())
    dp= {0:0}
    for i in range(n+1):
        for dig in str(i):
            dp[i]= min(dp.get(i,inf),dp.get(i-int(dig),inf)+1)
    print(dp[n])
main()