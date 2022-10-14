# 점심 식사시간
# dp로 풀어보자
# 오답 (49/50)
# 접근 방향을 고려해야 함

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
                    if board[ny][nx] == 0 and (nx, ny) not in stair_position:
                        board[ny][nx] = next_val
                        stairs.append([nx, ny, next_val])
                    # 방문한 지역인 경우 최솟값 갱신일 때만 연산
                    elif next_val < graph[ny][nx]:
                        board[ny][nx] = val


# 몇 명(번호 기준)의 사람을 뽑을지 결정
def combination(arr, k, idx):
    global combi_case
    if len(arr) == k:
        combi_case.append(list(arr))
        return
    for next_idx in range(idx, len(people)):
        arr.append(next_idx)
        combination(arr, k, next_idx+1)
        arr.pop()


# 각 경우의 수 별 계단 이용 시간 계산
def calculation(arr, idx, stairtime):
    while idx + 3 < len(arr):
        # 계단에 한 번에 4명 이상 몰리는 경우
        if arr[idx] + stairtime > arr[idx+3]:
            wait = arr[idx] + stairtime - arr[idx+3]
            arr[idx+3] += wait
        idx += 1
    return arr


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
    total = (n ** 2) * len(people)    # 총 소요 시간

    # 계단 좌표와 사람 좌표 추가
    for col in range(n):
        for row in range(n):
            # 사람인 경우
            if graph[col][row] == 1:
                people.append((row, col))
            # 계단인 경우
            elif graph[col][row] > 1:
                stair_info.append([row, col, graph[col][row]+1])

    x1, y1, case_1 = stair_info[0]
    c1_board = [[0] * n for _ in range(n)]
    x2, y2, case_2 = stair_info[1]
    c2_board = [[0] * n for _ in range(n)]
    stair_position = [(x1, y1), (x2, y2)]

    bfs([x1, y1, case_1], c1_board)
    bfs([x2, y2, case_2], c2_board)

    # 사람 위치 좌표를 기준으로 [1번 계단, 2번 계단] 이용 시간 저장
    result = []
    for px, py in people:
        result.append([c1_board[py][px], c2_board[py][px]])

    # 계단 이용 경우의 수 도출
    combi_case = [[]]
    for i in range(1, len(people)+1):
        combination([], i, 0)

    # 최단 시간 반환
    answer = (n**2) * len(people)
    s1_time = case_1 - 1    # 계단 1 이용 시간
    s2_time = case_2 - 1   # 계단 2 이용 시간

    people_count = set(range(len(people)))
    for c in combi_case:
        combi_case2 = list(people_count - set(c))
        s1_occupy = []  # 계단 1 상태
        s2_occupy = []  # 계단 2 상태

        for num_1 in c:
            next_people = result[num_1][0]
            s1_occupy.append(next_people)

        # 오름차순 정렬
        s1_occupy.sort(reverse=False)
        
        for num_2 in combi_case2:
            # 이용자가 너무 많이 몰리면 경우의 수 고려 X
            next_people = result[num_2][1]
            s2_occupy.append(next_people)

        # 오름차순 정렬
        s2_occupy.sort(reverse=False)

        # 계단 이용 시간 체크
        if 4 <= len(s1_occupy):
            calculation(s1_occupy, 0, s1_time)

        if 4 <= len(s2_occupy):
            calculation(s2_occupy, 0, s2_time)

        s1_total = s1_occupy[-1] if s1_occupy else 0
        s2_total = s2_occupy[-1] if s2_occupy else 0
        total = max(s1_total, s2_total)
        if total < answer:
            answer = total

    print(f'#{tc}', answer)
