# 15th_study

### 알고리즘 스터디 15주차

[백준 문제집](https://www.acmicpc.net/problem/1949) <br/>

<!-- [프로그래머스](https://school.programmers.co.kr/learn/courses/30/lessons/148653) -->

# [우수마을]

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

### [민웅](./우수마을/민웅.py)

```py
# 1949_우수마을_Great Village
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(node):

    for next in adjL[node]:
        if not visited[next]:
            visited[next] = 1
            dfs(next)
            dp[node][0] = dp[node][0] + max(dp[next][0], dp[next][1])
            dp[node][1] = dp[node][1] + dp[next][0]



N = int(input())
residents = list(map(int, input().split()))

adjL = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][1] = residents[i-1]

visited = [0] * (N+1)

for _ in range(N-1):
    s, g = map(int, input().split())
    adjL[s].append(g)
    adjL[g].append(s)

visited[1] = 1
dfs(1)

print(max(dp[1]))

```

### [병국](./우수마을/병국.py)

```py

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




```

### [상미](./우수마을/상미.py)

```py


```

### [성구](./우수마을/성구.py)

```py


```

</div>

</details>

<br><br>
