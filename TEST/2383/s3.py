# 점심 식사시간


import sys

sys.stdin = open('debug.txt')
# sys.stdin = open('sample_input.txt')

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


# 몇 명(번호 기준)의 사람을 뽑을지 결정
def combination(arr, k, idx):
    global combi_case
    if len(arr) == k:
        combi_case.append(list(arr))
        return
    for next_idx in range(idx, len(people)):
        arr.append(next_idx)
        combination(arr, k, next_idx + 1)
        arr.pop()


# 각 경우의 수 별 계단 이용 시간 계산
def calculation(arr, stairtime):
    elapsed_time = 0
    in_stairs = deque([])
    arr = deque(arr)

    # 계단에 사람 채우기(첫 번째 분기용)
    while len(in_stairs) < 3:
        if arr:
            new_value = arr.popleft()
            in_stairs.append(new_value + stairtime + 1)
        else:
            break

    # 두 번째 주기부터 이하 반복
    while arr or in_stairs:
        # 계단에 있는 사람이 내려가는 시간 계산
        is_valid = True
        for d in range(len(in_stairs)):
            in_stairs[d] -= 1
            if in_stairs[d] <= 0:
                is_valid = False

        # 계단을 다 내려간 사람이 있는 경우
        if not is_valid:
            replacement = []
            for descending in in_stairs:
                if descending > 0:
                    replacement.append(descending)
            in_stairs = replacement

        # 경과 시간 계산
        elapsed_time += 1

        # 결손 인원 보충
        while len(in_stairs) < 3:
            if arr and arr[0] <= 0:
                arr.popleft()
                in_stairs.append(stairtime)
            else:
                break

        # 대기 인원 정보 변경
        for a in range(len(arr)):
            arr[a] -= 1
                    
    return elapsed_time


# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    # 1번 계단 입력 여부
    stair1 = False

    # 사람 위치(x, y)
    people = []

    # 지도 정보
    graph = [list(map(int, input().split())) for _ in range(n)]
    stair_info = []  # 계단 위치
    total = (n**2) * len(people)  # 총 소요 시간

    # 계단 좌표와 사람 좌표 추가
    for col in range(n):
        for row in range(n):
            # 사람인 경우
            if graph[col][row] == 1:
                people.append((row, col))
            # 계단인 경우
            elif graph[col][row] > 1:
                stair_info.append([row, col, graph[col][row]])

    x1, y1, s1_time = stair_info[0]
    x2, y2, s2_time = stair_info[1]

    distance1 = []  # 계단 1까지의 거리
    distance2 = []  # 계단 2까지의 거리
    for px, py in people:
        dx_1 = abs(x1 - px)
        dx_2 = abs(x2 - px)
        dy_1 = abs(y1 - py)
        dy_2 = abs(y2 - py)
        distance1.append(dx_1 + dy_1)
        distance2.append(dx_2 + dy_2)

    # 계단 이용 경우의 수 도출
    combi_case = [[]]
    for i in range(1, len(people) + 1):
        combination([], i, 0)

    answer = 99999999   # 최단 시간 반환용

    people_count = set(range(len(people)))
    for case1 in combi_case:
        case_total = []
        case2 = list(people_count - set(case1))
        stair1_case = []        # 계단 1까지 가는 데 걸리는 시간
        stair2_case = []        # 계단 2까지 가는 데 걸리는 시간
        if case1:
            for c1 in case1:
                stair1_case.append(distance1[c1])
            stair1_case.sort(reverse=False)
            case_total.append(calculation(stair1_case, s1_time))

        if case2:
            for c2 in case2:
                stair2_case.append(distance2[c2])
            stair2_case.sort(reverse=False)
            case_total.append(calculation(stair2_case, s2_time))

        total = max(case_total)
        if total < answer:
            answer = total

    print(f'#{tc}', answer)
