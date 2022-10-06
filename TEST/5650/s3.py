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

# 런타임 에러 대응
import sys
sys.stdin = open('debug2.txt')

# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 블록 번호별 방향 반전
# 각 블록 별 진입 방향 경우의 수 : (), (2, 3), (3, 0), (0, 1), (1, 2)
dir_change = [(4, 4), (0, 1), (1, 2), (2, 3), (3, 0), (4, 4)]


def dfs(x, y, direction):
    global answer
    score = 0

    # 좌표 이동
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 원점으로 되돌아온 경우
        if nx == start_x and ny == start_y:
            if answer < score:
                answer = score
            return
        
        # 인덱스 범위가 유효한 경우
        if 0 <= nx < width and 0 <= ny < width:
            # 다음 자리가 0인 경우 계속 이동
            if board[ny][nx] == 0:
                x = nx
                y = ny
                continue
            # 0이 아닌 경우 이동할 위치 정보 수집
            current_val = board[ny][nx]

            # 웜홀로 이동하는 경우
            if current_val >= 6:
                # 웜홀 출구 인덱스를 index()로 찾으려고 하니까 런타임 에러가 발생한다.
                exit_idx = current_val - 5 if wormhole[current_val] == (nx, ny) else current_val
                x, y = wormhole[exit_idx]
            # 1~5번 블록에 가는 경우
            elif current_val > 0:
                next_dir = (direction + 2) % 4      # 이동 방향 전환(기본 = 반전)
                for k in range(2):
                    # 1~4번 블록이고 진입 방향이 방향전환 가능한 방향이면 방향 전환
                    turn_check = (direction + 2) % 4
                    if turn_check == dir_change[current_val][k]:
                        direction = dir_change[current_val][1] if k == 0 else dir_change[current_val][0]
                        score += 1
                        x = nx
                        y = ny
                        break
                else:       # 방향 반전인 경우
                    score = score * 2 + 1
                    if answer < score:
                        answer = score
                    return
            # 블랙홀에 가는 경우
            else:
                if answer < score:
                    answer = score
                return

        # 인덱스 범위를 벗어나려 하는 경우(벽에 박는 경우)
        # 벽에 부딪히면 방향 전환, 점수 + 1
        else:
            score = score * 2 + 1
            if answer < score:
                answer = score
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
                start_x = row
                start_y = col
                for d in range(4):
                    dfs(row, col, d)

    print(f'#{tc}', answer)
