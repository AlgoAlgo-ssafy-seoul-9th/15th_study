# 2933_미네랄_minerals
import sys
from collections import deque
# input = sys.stdin.readline
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 클러스터 내리기
def fall(cluster_lst):
    falling_length = float('inf')

    for x, y in cluster_lst:
        cnt = 0
        while True:
            if x+1 > R-1:
                break
            if cave[x+1][y] == '.':
                cnt += 1
            else:
                break

            x += 1

        if cnt < falling_length and cnt != 0:
            falling_length = cnt

    for x, y in cluster_lst:
        cave[x][y] = '.'

    for x, y in cluster_lst:
        cave[x+falling_length][y] = 'x'

# 떨어져야하는 클러스터 체크
def mineral_down(x, y):
    global cave

    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx <= R-1 and 0 <= ny <= C-1:
            if cave[nx][ny] == 'x':
                columns = [ny]
                falling_check = []
                visited = [[0]*C for _ in range(R)]
                cluster = []
                visited[nx][ny] = 1
                if nx != R-1:
                    if cave[nx+1][ny] == '.':
                        falling_check.append(ny)
                cluster.append([nx, ny])
                q = deque()
                q.append([nx, ny])

                while q:
                    lx, ly = q.popleft()

                    for di in dxy:
                        nlx = lx + di[0]
                        nly = ly + di[1]

                        if 0 <= nlx <= R-2 and 0 <= nly <= C-1:
                            if cave[nlx][nly] == 'x' and not visited[nlx][nly]:
                                q.append([nlx, nly])
                                cluster.append([nlx, nly])
                                visited[nlx][nly] = 1
                                if nly not in columns:
                                    columns.append(nly)
                                if cave[nlx+1][nly] == '.' and nly not in falling_check:
                                    falling_check.append(nly)
                falling_check.sort()
                columns.sort()
                if falling_check == columns:
                    fall(cluster)
                else:
                    continue


R, C = map(int, input().split())

cave = [list(input().strip()) for _ in range(R)]

N = int(input())
h_lst = deque(list(map(int, input().split())))
left_or_right = True


for _ in range(N):
    H = R - h_lst.popleft()
    if left_or_right:
        for i in range(C):
            if cave[H][i] == 'x':
                cave[H][i] = '.'
                mineral_down(H, i)
                break
        else:
            continue
    else:
        for i in range(C-1, -1, -1):
            if cave[H][i] == 'x':
                cave[H][i] = '.'
                mineral_down(H, i)
                break
        else:
            continue

    left_or_right = not left_or_right

for c in cave:
    print(*c, sep='')
