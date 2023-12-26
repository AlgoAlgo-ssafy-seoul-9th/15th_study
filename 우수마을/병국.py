# 우수마을아닐때, 우수마을일때
import sys
sys.setrecursionlimit(10**6)
def dfs(num):
    v[num] = 1
    for neighbor in graph[num]:
       if v[neighbor] != 1:
           dfs(neighbor)
           # 현재마을 우수마을 + 이웃마을 우수마을X
           dp[num][1] += dp[neighbor][0]
           # 현재 마을 우수마을X => 이웃마을 우수O or 우수 X max로
           dp[num][0] += max(dp[neighbor][0],dp[neighbor][1])




n = int(input())
arr = [0] + list(map(int,input().split()))
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    con1, con2 = map(int,input().split())
    graph[con1].append(con2)
    graph[con2].append(con1)
dp = [[0,0]] + [[0,arr[i]] for i in range(1,n+1)]
# print(dp)
v = [0] * (n+1)

dfs(1)
print(max(dp[1][0],dp[1][1]))



