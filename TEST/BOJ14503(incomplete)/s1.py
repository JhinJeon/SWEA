# 로봇 청소기

# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def robot_algorithm(x, y, dir):
    # 1. 왼쪽 방향에 청소(방문)하지 않은 공간이 있는 경우
    visited[y][x] = True

    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0 and not visited[ny][nx]:
        robot_algorithm(nx, ny, dir)
    # 바라보는 방향에 청소할 자리가 없으면 시계 방향으로 회전
    else:
        for d in range(1, 4):
            next_dir = (dir + d) % 4
            nx = x + dx[next_dir]
            ny = y + dy[next_dir]
            if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 0 and not visited[ny][nx]:
                robot_algorithm(nx, ny, next_dir)
                return
        else:
            return


    # 4. 후진도 불가능한 경우
    return


n, m = map(int, input().split())
robot_x, robot_y, head = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]