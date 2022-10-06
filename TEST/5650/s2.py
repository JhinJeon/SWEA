# 핀볼 게임

# 블록 모양:
# 1. 위/오른쪽 방향 튕기기(0,1)
# 2. 아래/오른쪽 방향 튕기기(1,2)
# 3. 왼쪽/아래 방향 튕기기(2,3)
# 4. 왼쪽/위 방향 튕기기(3,0)
# 5. 온 방향의 역뱡향으로 튕기기
# 웜홀 = 6~10
# 블랙홀 = -1
# 벽이나 블록(웜홀, 블랙홀 X)에 박으면 +1점

# 재귀함수로 구현하면 최대 깊이 초과 문제 발생
import sys
sys.stdin = open('debug.txt')

# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 블록 번호별 방향 반전
# 각 블록 별 진입 방향 경우의 수 : (), (2, 3), (3, 0), (0, 1), (1, 2)
dir_change = [(4, 4), (0, 1), (1, 2), (2, 3), (3, 0), (4, 4)]


def dfs(x, y, direction):
    score = 0

    # 좌표 이동
    while True:
        x += dx[direction]
        y += dy[direction]

        # 출발 지점으로 돌아온 경우
        if (x_start, y_start) == (x, y):
            return score

        # 인덱스 범위가 유효한 경우
        if 0 <= x < width and 0 <= y < width:
            # 다음 자리가 0인 경우 계속 이동
            if board[y][x] == 0:
                continue
            # 0이 아닌 경우 이동할 위치 정보 수집
            current_val = board[y][x]

            # 웜홀로 이동하는 경우
            if current_val >= 6:
                enter_idx = (wormhole.index((x, y)) + 5) % 10
                x, y = wormhole[enter_idx]
            # 1~5번 블록에 가는 경우
            elif current_val > 0:
                next_dir = (direction + 2) % 4      # 이동 방향 전환(기본 = 반전)
                for k in range(2):
                    # 1~4번 블록이고 진입 방향이 방향전환 가능한 방향이면 방향 전환
                    turn_check = (direction + 2) % 4
                    if turn_check == dir_change[current_val][k]:
                        next_dir = dir_change[current_val][1] if k == 0 else dir_change[current_val][0]
                        break
                # 방향 회전 결과 적용, 점수 + 1
                direction = next_dir
                score += 1
            # 블랙홀에 가는 경우
            else:
                return score

        # 인덱스 범위를 벗어나려 하는 경우(벽에 박는 경우)
        # 벽에 부딪히면 방향 전환, 점수 + 1
        else:
            direction = (direction + 2) % 4
            score += 1


t = int(input())

for tc in range(1, t+1):
    width = int(input())                    # 게임판 너비
    wormhole = [() for _ in range(11)]      # 웜홀 좌표 저장(1~5, 6~10)
    board = [list(map(int, input().split())) for _ in range(width)]

    # 웜홀 정보 추가(x좌표, y좌표)
    for col in range(width):
        for row in range(width):
            idx = board[col][row]
            if idx >= 6:
                # 입구 정보가 없으면 입구부터 추가
                entrance = idx - 5
                if not wormhole[entrance]:
                    wormhole[entrance] = (row, col)
                # 입구 정보가 있으면 출구 추가
                else:
                    wormhole[idx] = (row, col)

    # 0부터 출발
    answer = 0
    for col in range(width):
        for row in range(width):
            if board[col][row] == 0:
                x_start, y_start = row, col
                for d in range(4):
                    result = dfs(row, col, d)
                    if result > answer:
                        answer = result

    print(f'#{tc}', answer)
