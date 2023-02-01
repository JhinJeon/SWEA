# 2048 (Easy)
import sys
sys.stdin = open('sample_input.txt')

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

max_number = 2  # 블록의 최댓값


# 그래프가 갱신될 때마다 최댓값을 갱신하는 함수
def get_max_number(graph):   # graph = board, k = 보드의 크기(n)
    global max_number
    for col in range(n):
        for row in range(n):
            if graph[col][row] > max_number:
                max_number = graph[col][row]


# dfs로 모든 이동 경우의 수를 찾는 함수
def dfs_board(graph, trials):   # graph = board, trials = 남은 이동 횟수
    # print(trials,graph)
    if trials == 0:
        get_max_number(graph)
        return
    pull_to_top = graph.copy()
    pull_to_right = graph.copy()
    pull_to_bot = graph.copy()
    pull_to_left = graph.copy()

    # 위쪽으로 밀기
    for row in range(n):
        for col in range(n-1):
            # 0이 아닌 블록인 경우
            if pull_to_top[col][row] > 0:
                # 공백이 아닌 블록을 발견할 때까지 1칸씩 아래로 탐색
                for new_col in range(col+1, n):
                    if pull_to_top[new_col][row] > 0:
                        # 같은 숫자일 경우 합체(아래쪽 블록은 0)
                        if pull_to_top[new_col][row] == pull_to_top[col][row]:
                            pull_to_top[col][row] *= 2
                            pull_to_top[new_col][row] = 0
                        # 다른 숫자일 경우 바로 아래쪽에 붙이기
                        elif new_col != col + 1:
                            pull_to_top[col + 1][row] = pull_to_top[new_col][row]
                            pull_to_top[new_col][row] = 0
                        break

            # 0인 블록인 경우 위쪽으로 이동만(합체 X)
            else:
                for new_col in range(col+1, n):
                    if pull_to_top[new_col][row] > 0:
                        pull_to_top[col][row] = pull_to_top[new_col][row]
                        pull_to_top[new_col][row] = 0
                        break

    # 위쪽으로 미는 작업을 마치면 재귀호출
    dfs_board(pull_to_top, trials-1)

    # 왼쪽으로 밀기
    for col in range(n):
        for row in range(n-1):
            # 0이 아닌 블록을 발견한 경우
            if pull_to_left[col][row] > 0:
                # 공백이 아닌 블록을 찾을 때까지 한 칸씩 오른쪽으로 탐색
                for new_row in range(row+1, n):
                    if pull_to_left[col][new_row] > 0:
                        # 똑같은 수의 블록이면 합체
                        if pull_to_left[col][row] == pull_to_left[col][new_row]:
                            pull_to_left[col][row] *= 2
                            pull_to_left[col][new_row] = 0

                        # 다른 숫자면 이동(단, 발견한 블록 위치가 추가 탐색 시작 위치와 동일하면 이동하지 않음)
                        elif row+1 != new_row:
                            pull_to_left[col][row +1] = pull_to_left[col][new_row]
                            pull_to_left[col][new_row] = 0

                        break

            # 0인 블록을 발견한 경우 왼쪽으로 이동만(합체 X)
            else:
                for new_row in range(row+1, n):
                    if pull_to_left[col][new_row] > 0:
                        pull_to_left[col][row] = pull_to_left[col][new_row]
                        pull_to_left[col][new_row] = 0
                        break

    # 왼쪽으로 미는 작업을 마치면 재귀호출
    dfs_board(pull_to_left, trials-1)

    # 오른쪽으로 밀기
    for col in range(n):
        for row in range(n-1, 0, -1):
            # 0이 아닌 블록을 발견한 경우
            if pull_to_right[col][row] > 0:
                # 공백이 아닌 블록을 찾을 때까지 한 칸씩 왼쪽으로 탐색
                for new_row in range(row-1, -1, -1):
                    if pull_to_right[col][new_row] > 0:
                        # 왼쪽 블록과 오른쪽 블록이 같으면 오른쪽 블록은 2배, 왼쪽 블록은 0
                        if pull_to_right[col][row] == pull_to_right[col][new_row]:
                            pull_to_right[col][row] *= 2
                            pull_to_right[col][new_row] = 0

                        # 다른 숫자일 경우 바로 왼쪽에 붙이기(단, 같은 위치를 가리키는 경우 이동하지 않음)
                        elif new_row != row-1:
                            pull_to_right[col][row - 1] = pull_to_right[col][new_row]
                            pull_to_right[col][new_row] = 0

                        break

            # 0인 블록인 경우 왼쪽에서 오른쪽으로 이동만(합체 X)
            else:
                for new_row in range(row-1, -1, -1):
                    if pull_to_right[col][new_row] > 0:
                        pull_to_right[col][row] = pull_to_right[col][new_row]
                        pull_to_right[col][new_row] = 0
                        break

    dfs_board(pull_to_right, trials-1)

    # 아래쪽으로 밀기
    for row in range(n):
        for col in range(n-1, 0, 1):
            # 0이 아닌 블록을 발견한 경우
            if pull_to_bot[col][row] > 0:
                # 공백이 아닌 블록을 찾을 때까지 한 칸씩 위쪽으로 탐색
                for new_col in range(col-1, -1, -1):
                    if pull_to_bot[new_col][row] > 0:
                        if pull_to_bot[new_col][row] == pull_to_bot[col][row]:
                            pull_to_bot[col][row] *= 2
                            pull_to_bot[new_col][row] = 0
                        elif col-1 != new_col:
                            pull_to_bot[col-1][row] = pull_to_bot[new_col][row]
                            pull_to_bot[new_col][row] = 0
                    break

            # 0인 블록을 발견한 경우 아래쪽으로 이동만
            else:
                for new_col in range(col-1, -1, -1):
                    if pull_to_bot[new_col][row] > 0:
                        pull_to_bot[col][row] = pull_to_bot[new_col][row]
                        pull_to_bot[new_col][row] = 0
                        break

    dfs_board(pull_to_bot, trials-1)


dfs_board(board, 5)

print(max_number)
