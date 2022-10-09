# 점심 식사시간
# dp로 풀어보자
import sys
sys.stdin = open('sample_input.txt')

from collections import deque


def bfs(arr, board):
    stairs = deque([])
    stairs.append(arr)
    # 계단 위치를 기준으로 BFS 탐색
    while stairs:
        for _ in range(len(stairs)):
            x, y, val = stairs.popleft()
            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                next_val = val + 1
                # 유효한 좌표 범위인 경우
                if 0 <= nx < n and 0 <= ny < n:
                    # 아직 방문하지 않은 지역인 경우(계단 제외)
                    if board[ny][nx] == 0:
                        board[ny][nx] = next_val
                        stairs.append([nx, ny, next_val])
                    # 방문한 지역인 경우 최솟값 갱신일 때만 연산
                    elif next_val < graph[ny][nx]:
                        board[ny][nx] = val


def combination(arr, k, idx):
    global combi_case
    if len(arr) == k:
        combi_case.append(list(arr))
        return
    for next_idx in range(idx, len(people)):
        arr.append(people[next_idx])
        combination(arr, k, next_idx)
        arr.pop()


# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    # 1번 계단 입력 여부
    stair1 = False

    # 사람 위치(x, y)
    people = []

    # 지도 정보
    graph = [list(map(int,input().split())) for _ in range(n)]
    stair_info = []

    # 계단 좌표와 사람 좌표 추가
    for col in range(n):
        for row in range(n):
            # 사람인 경우
            if graph[col][row] == 1:
                people.append((row, col))
            # 계단인 경우
            elif graph[col][row] > 1:
                stair_info.append([row, col, graph[col][row]+1])

    case_1 = stair_info[0]
    c1_board = [[0] * n for _ in range(n)]
    case_2 = stair_info[1]
    c2_board = [[0] * n for _ in range(n)]

    bfs(case_1, c1_board)
    bfs(case_2, c2_board)

    # 사람 위치 좌표를 기준으로 [1번 계단, 2번 계단] 이용 시간 저장
    result = []
    for px, py in people:
        result.append([case_1[py][px], case_2[py][px]])

    # 계단 이동 경우의 수 도출
    combi_case = []
    for i in range(1,len(people)+1):
        combination([], i, 0)

    # 최단 시간 반환
    answer = (n**2) * len(people)
    for c in combi_case:
        result = 0
        combi_case2 = list(set(people) - set(c))
        for x1, y1 in c:
            result += graph[y1][x1]
        for x2, y2 in combi_case2:
            result += graph[y2][x2]
        if result < answer:
            answer = result

    print(f'#{tc}', answer)