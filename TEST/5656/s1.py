# 벽돌 깨기
import sys
sys.stdin = open('sample_input.txt')
# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 벽돌 파괴 경우의 수 계산
def dfs(current_graph, lives):
    global answer, initial_blocks
    # 벽돌 기회가 있는 경우
    if lives > 0:
        for col in range(height):
            for row in range(width):
                if graph[col][row] > 1:
                    next_graph = current_graph.copy()
                    explode(next_graph, row, col)
                    dfs(destroyed(next_graph), lives - 1)
                    
    # 최종 결과 계산(살아남은 블록 수 세기)
    survived_blocks = 0
    for h in range(height):
        for w in range(width):
            if current_graph[h][w] > 0:
                survived_blocks += 1
    if survived_blocks - lives < answer:
        answer = survived_blocks
    return

            
# 벽돌 파괴 계산
def explode(sample_graph, x, y):
    radius = sample_graph[y][x]
    sample_graph[y][x] = 0
    for dir in range(4):
        for r in range(1, radius):
            nx = x + dx[dir] * r
            ny = y + dy[dir] * r
            if 0 <= nx < width and 0 <= ny < height:
                # 중간에 값이 2 이상인 블록이 있으면 연쇄 폭발
                if sample_graph[ny][nx] > 1:
                    explode(sample_graph, nx, ny)
                # 값이 1인 블록이면 재귀 호출 X
                elif sample_graph[ny][nx] == 1:
                    sample_graph[ny][nx] = 0


# 파괴된 상태를 반영하는 함수
def destroyed(destroyed_graph):
    for row in range(width):
        for col in range(height-1, 0, -1):
            if destroyed_graph[col][row] == 0:
                gap = []    # 공백 y좌표 기억
                for blankcheck in range(col, 0, -1):
                    if destroyed_graph[blankcheck][row] != 0:
                        break
                    gap.append(blankcheck)
                # destroyed_graph 맨 위까지 온 경우
                else:
                    continue

                # gap 위의 블록이 gap_length 칸 만큼 아래로 내려오도록 하기
                if len(gap) > 0:
                    g = gap[0]
                    block_status = g - len(gap)
                    destroyed_graph[g][row], destroyed_graph[block_status][row] = destroyed_graph[block_status][row], destroyed_graph[g][row]

    return destroyed_graph


t = int(input())

for tc in range(1,t+1):
    # 각각 시도 횟수, 너비, 높이
    trial, width, height = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(height)]

    initial_blocks = 0  # 최초 graph의 블록 수
    for col in range(height):
        for row in range(width):
            if graph[col][row] > 0:
                initial_blocks += 1

    answer = initial_blocks     # 남은 벽돌 수
    dfs(graph, trial)

    print(f'#{tc}', answer)