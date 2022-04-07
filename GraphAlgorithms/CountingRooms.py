import sys
sys.setrecursionlimit(1000000)
from collections import defaultdict,Counter
visited = defaultdict(Counter)

a,b = map(int,input().split())
matriz = [input() for _ in range(a)]

def dfs(n,m):
    if not visited[n][m]:
        
        visited[n][m] = 1
        #UP
        if n > 0 and 0<=m<=len(matriz[0])-1 :
            if matriz[n-1][m] ==".":
                dfs(n-1,m)
        # DOWN
        if n < len(matriz)-1 and 0<=m<=len(matriz[0])-1:
            if matriz[n+1][m] ==".":
                dfs(n+1,m)
        # LEFT
        if m > 0 and 0<=n<=len(matriz)-1:
            if matriz[n][m-1] == ".":
                dfs(n,m-1)
            
        # RIGHT
        if m < len(matriz[0])-1 and 0<=n<=len(matriz)-1:
            if matriz[n][m+1] == ".":
                dfs(n,m+1)
        



def solver(n,m):
    ans = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and matriz[i][j]!="#":
                ans +=1
                dfs(i,j)    
    return ans



print(solver(a,b))


