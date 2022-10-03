# 재미있는 오셸로 게임
import sys
sys.stdin = open('sample_input.txt')

# 위쪽부터 시계방향
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

t = int(input())

for tc in range(1, t+1):
    board_width, playcount = map(int,input().split())
    board = [[0] * board_width for _ in range(board_width)]

    # 보드 초기 설정
    standard = board_width//2
    # 2 = 백돌, 1 = 흑돌
    board[standard][standard] = 2
    board[standard-1][standard-1] = 2
    board[standard - 1][standard] = 1
    board[standard][standard - 1] = 1

    for p in range(playcount):
        col, row, color = map(int,input().split())
        # 행, 열 좌표값 보정(인덱스 에러 방지)
        col -= 1
        row -= 1
        # 돌 새로 두기 : 둘 자리에 아무 돌도 없으면 플레이 가능
        if board[col][row] == 0:
            board[col][row] = color
            
            # 돌을 새로 둔 위치를 기준으로 땅따먹기
            for direction in range(8):
                change_color = []  # 색깔 바꿀 좌표
                nx = row + dx[direction]
                ny = col + dy[direction]
                while True:
                    # 유효하지 않은 좌표 or 빈 땅에 땅따먹기를 시도하는 경우 즉시 중단
                    if ny < 0 or ny >= board_width or nx < 0 or nx >= board_width or board[ny][nx] == 0:
                        change_color = []
                        break
                    # 같은 색깔 돌 만나면 탐색 중단
                    elif board[ny][nx] == color:
                        break
                    # 이상 없으면 같은 방향으로 계속 땅따먹기 시도
                    change_color.append((ny, nx))
                    nx += dx[direction]
                    ny += dy[direction]
                
                # 색상 반전 적용
                for cy, cx in change_color:
                    board[cy][cx] = color

    # 결과 정산
    black = 0   # 1 = 흑돌
    white = 0   # 2 = 백돌
    for col in range(board_width):
        for row in range(board_width):
            if board[col][row] == 1:
                black += 1
            elif board[col][row] == 2:
                white += 1

    print(f'#{tc}', black, white)