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
