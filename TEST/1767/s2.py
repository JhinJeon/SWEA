# 프로세서 연결하기

import sys
sys.stdin = open('sample_input.txt')

# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# dfs의 탐색 결과 되돌리기(유효하지 않은 경로)
def counter_dfs(x, y, direction):
    nx = x + dx[direction]
    ny = y + dy[direction]
    if 0 <= nx < n and 0 <= ny < n:
        if graph[ny][nx] != -1:
            return
        else:
            graph[ny][nx] = 0
            counter_dfs(nx, ny, direction)


# 차례대로 탐색 깊이, 연결된 셀 개수, 전선 길이
def case_calculate(depth, connected_cells):
    global cell, answer
    length = 0
    for i in range(n):
        length += graph[i].count(-1)
    # 모든 셀을 탐색한 경우
    if depth == len(cell_status):
        # 연결된 셀 개수가 더 많은 사례를 발견한 경우
        if connected_cells > cell:
            cell = connected_cells
            answer = length
        # 연결된 셀 개수가 동일하지만 전선 길이가 더 짧은 사례를 발견한 경우
        elif connected_cells == cell and length < answer:
            answer = length
        return
    else:
        # 개선의 여지가 없는 경우
        if connected_cells + len(cell_status) - depth < cell and length > answer:
            return
        for d in range(4):
            x = cell_status[depth][0]
            y = cell_status[depth][1]
            error = False   # d 방향으로 이동했을 때 전선이나 다른 코어에 걸리는지 확인

            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                # 다른 코어나 전선을 만난 경우
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[ny][nx] != 0:
                        error = True
                        break
                # 벽에 닿은 경우
                else:
                    break
                graph[ny][nx] = -1
                x = nx
                y = ny

            if error:
                counter_dfs(nx, ny, (d+2) % 4)
                # 아직 모든 방향을 탐색하지 않은 경우 다른 방향부터 시도
                if d < 3:
                    continue
            else:
                connected_cells += 1
            case_calculate(depth + 1, connected_cells)
            if not error:
                connected_cells -= 1
            counter_dfs(nx, ny, (d+2) % 4)


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    cell_status = []    # 셀이 위치한 좌표(dfs 탐색용)
    cell = 0  # 연결된 셀 개수
    answer = n ** 2          # 전선 길이

    # 셀 정보 추가
    for col in range(n):
        for row in range(n):
            if graph[col][row] == 1:
                # 벽에 붙어있는 셀인 경우 case_calculate에서 계산하지 않고 연결된 개수 +1
                if col == 0 or row == 0:
                    cell += 1
                # 벽에 붙어있지 않은 셀인 경우 case_calculate에서 계산
                else:
                    cell_status.append((row, col))

    case_calculate(0, cell)

    print(f'#{tc}', answer)
