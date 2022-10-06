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
sys.stdin = open('sample_input.txt')

# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 블록 번호별 방향 반전
# 각 블록 별 진입 방향 경우의 수 : (), (2, 3), (3, 0), (0, 1), (1, 2)
dir_change = [(), (0, 1), (1, 2), (2, 3), (3, 0), (4, 4)]


def dfs(x, y, direction, score):
    global answer, visited_start
    # 시작 지점으로 되돌아온 경우
    if (x_start, y_start) == (x, y) and visited_start:
        if answer < score:
            answer = score
        return

    visited_start = True
    # 다음 좌표 설정
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < width and 0 <= ny < width:
        next_val = board[ny][nx]    # 다음 좌표의 값 정보
        # 웜홀로 가는 경우
        if next_val >= 6:
            nx, ny = (wormhole.index((nx, ny)) + 5) % 11
            dfs(nx, ny, direction, score)
        # 블록에 가는 경우
        elif next_val > 0:
            if next_val <= 5:   # 1~5번 블록인 경우
                for k in range(2):
                    # 1~4번 블록이고 진입 방향이 방향전환 가능한 방향이면 방향 전환
                    turn_check = (direction + 2) % 4
                    if turn_check == dir_change[next_val][k]:
                        next_dir = dir_change[next_val][1] if k == 0 else dir_change[next_val][0]
                        break
                # 그 외의 경우 방향 반전
                else:
                    next_dir = (direction + 2) % 4
            dfs(nx, ny, next_dir, score + 1)
        # 블랙홀에 가는 경우
        elif next_val < 0:
            if answer < score:
                answer = score
            return
        # 그 외의 경우(빈 공간)
        else:
            dfs(nx, ny, direction, score)
    # 벽에 부딪히는 경우 현재 위치에서 방향 전환, 점수 + 1
    else:
        next_dir = (direction+2) % 4
        dfs(x, y, next_dir, score + 1)
    return


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
                    visited_start = False
                    dfs(row, col, d, 0)

    print(f'#{tc}', answer)
