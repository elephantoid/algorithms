import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global ans
    if a[x][y] == 0:
        a[x][y] = 2
        ans += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if a[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if a[nx][ny] == 1:
        return
    clean(nx, ny, d)


n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
clean(x, y, d)
print(ans)

#----------------------------------------------------------
#bfs 방식
import sys
from collections import deque

# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def change(d): # 방향 전환
    if d == 0:  # 북 -> 서
        return 3
    elif d == 1:  # 동 -> 북
        return 0
    elif d == 2:  # 남 -> 동
        return 1
    elif d == 3:  # 서 -> 동
        return 2
def back(d): # 후진
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1

def bfs(row, col, d):
    cnt = 1  # 청소하는 칸의 개수
    arr[row][col] = 2
    q = deque([[row, col, d]])

    # 큐가 비어지면 종료
    while q:
        row, col, d = q.popleft()
        temp_d = d

        for i in range(4):
            temp_d = change(temp_d)
            new_row, new_col = row + dy[temp_d], col + dx[temp_d]

            # a
            if 0 <= new_row < N and 0 <= new_col < M and arr[new_row][new_col] == 0:
                cnt += 1
                arr[new_row][new_col] = 2
                q.append([new_row, new_col, temp_d])
                break

            # c
            elif i == 3:  # 갈 곳이 없었던 경우
                new_row, new_col = row + dy[back(d)], col + dx[back(d)]
                q.append([new_row, new_col, d])

                # d
                if arr[new_row][new_col] == 1:  # 뒤가 벽인 경우
                    return cnt

if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())

    # 지도
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    # 탐색
    print(bfs(r, c, d))