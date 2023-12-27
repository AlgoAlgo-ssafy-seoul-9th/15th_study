## 백준_ 1949 우수마을

import sys
sys.setrecursionlimit(20000)        ## 10**6
input = sys.stdin.readline

n = int(input())
people = [0] + list(map(int, input().split()))
graph = [[] for i in range(n+1)]
dp = [[0, 0] for i in range(n+1)]
visited = [False for i in range(n+1)]

# dp[마을 번호][우수마을 아닐 때=0], dp[마을 번호][우수 마을일 때 = 1]
# DFS 돌리면서 dp에 우수 마을일때, 우수 마을이 아닐 때의 주민수의 최대값을 갱신

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    visited[x] = True
    dp[x][1] = people[x]
    for i in graph[x]:
        if not visited[i]:
            dfs(i)
            dp[x][0] += max(dp[i][0], dp[i][1])
            dp[x][1] += dp[i][0]

dfs(1)

print(max(dp[1][0], dp[1][1]))