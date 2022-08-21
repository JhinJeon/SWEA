# 델타 검색
import sys
sys.stdin = open('1in.txt')

# 순서대로 상, 우, 하, 좌 이동
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(x, y):
    val = 0
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[y][x] - graph[ny][nx] > 0:
                val += graph[y][x] - graph[ny][nx]
            else:
                val += graph[ny][nx] - graph[y][x]
    return val


for tc in range(1,11):
    n = int(input())
    answer = 0
    graph = [list(map(int,input().split())) for _ in range(n)]
    for col in range(n):
        for row in range(n):
            answer += dfs(row, col)

    print(f'#{tc} {answer}')