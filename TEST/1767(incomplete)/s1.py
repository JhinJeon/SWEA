# 프로세서 연결하기
# 해결 중

# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(x, y):
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    connected_cell = []
    core_position = []      # 코어 좌표
    for col in range(n):
        for row in range(n):
            if graph[col][row] == 1:
                core_position.append((row, col))


    print(f'#{tc}')