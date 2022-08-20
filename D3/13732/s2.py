# 정사각형 판정
import sys
sys.stdin = open('sample_input.txt')

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(input_graph, y, x):
    global block
    input_graph[y][x] = '.'
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n and input_graph[ny][nx] == '#':
            block += 1
            dfs(input_graph, ny, nx)


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    width = []
    height = []
    answer = 'yes'  # 기본값은 yes(조건 미충족 시 no)
    checked = False

    for col in range(n):
        for row in range(n):
            if graph[col][row] == '#':
                block = 1
                dfs(graph, col, row)
                if block**(1/2) != int(block**(1/2)) or checked:
                    answer = 'no'
                checked = True

    print(f'#{tc} {answer}')
