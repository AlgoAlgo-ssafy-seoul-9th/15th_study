# 1949 우수마을
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(now:int) -> None:
    for next in neighbor[now]:
        if not visited[next]:
            visited[next] = 1
            # 모두 돌고 나서 마지막 부터 dp 배열 저장
            dfs(next)
            # 지금 마을이 우수가 아니면 다음은 우수가 될 수 있고, 아닐 수도 있음
            dp[now][0] += max(dp[next][1], dp[next][0])
            # 지금 마을이 우수이면 다음은 우수일 수 없음
            dp[now][1] += dp[next][0]
    return


if __name__ == "__main__":
    N = int(input())
    population = [0]+list(map(int, input().split()))
    neighbor = [[] for _ in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        neighbor[a].append(b)
        neighbor[b].append(a)
    dp = [[0,population[i]] for i in range(N+1)]
    visited = [0] * (N+1)
    visited[1]=1
    dfs(1)
    print(max(dp[1]))
