# 격자판 칠하기
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())     # n = 세로 길이, m = 가로 길이
    board = [list(input()) for _ in range(n)]
    standard_odd = True    # '#'이 col + row 인덱스 값 합이 홀수인 칸에만 들어가는 경우
    point_odd = True # '.'이 col + row 인덱스 값 합이 홀수인 칸에만 들어가는 경우
    point_appeared = False
    answer = 'possible'
    for col in range(n):
        for row in range(m):
            # '.'이 col + row 인덱스 값 합이 짝수인 칸에만 들어가는 경우
            if board[col][row] == '.' and (col + row) % 2 == 0:
                point_odd = False
                point_appeared = True

            # '#'이 col + row 인덱스 값 합이 짝수인 칸에만 들어가는 경우
            if board[col][row] == '#' and (col + row) % 2 == 0:
                standard_odd = False

            # '.'이 col + row 인덱스 값 합이 홀수인 칸과 짝수인 칸에 같이 들어가는 경우
            if not point_odd and (col + row) % 2 == 1 and board[col][row] == '.':
                answer = 'impossible'
                break

            # '#'이 col + row 인덱스 값 합이 홀수인 칸과 짝수인 칸에 같이 들어가는 경우
            if not standard_odd and (col + row) % 2 == 1 and board[col][row] == '#':
                answer = 'impossible'
                break

            # '#', '.'이 모두 짝수 번째 칸에 들어가는 경우
            if not point_odd and not standard_odd:
                answer = 'impossible'
                break

        # 불가능 판정이면 반복문 즉시 종료
        if answer == 'impossible':
            break
            
    # 그래프에 '?'만 있는 경우가 아니라면 불가능 처리
    if point_appeared and standard_odd and point_odd:
        answer = 'impossible'
    print(f'#{tc} {answer}')
