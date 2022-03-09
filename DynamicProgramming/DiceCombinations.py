MOD = 10**9 + 7

def main():    
    n = int(input())
    ans = [0 for i in range(10**6 + 1)]
    ans[0] = 1

    for i in range(1,n+1):
        j = 1
        while j <= 6 and i - j >=0:
            ans[i] += ans[i-j]
            ans[i] = ans[i]%MOD
            j+=1
    print(ans[n])


main()