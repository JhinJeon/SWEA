#  어디에 단어가 들어갈 수 있을까

import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = []
    for i in range(n):
        puzzle.append(list(map(int, input().split())))
    answer = 0

    for col in range(n):  # 가로 인덱스
        streak = 0
        for row in range(n):
            if puzzle[col][row] == 1:
                streak += 1
            else:
                if streak == k:
                    answer += 1
                streak = 0
        if streak == k:
            answer += 1

    for row in range(n):
        streak = 0
        total = 0
        for col in range(n):  # 세로 인덱스
            if puzzle[col][row] == 1:
                streak += 1
            else:
                if streak == k:
                    answer += 1
                streak = 0
        if streak == k:
            answer += 1

    print("#" + str(test_case) + " " + str(answer))

'''
최적의 코드
# 그래프 모양 바꾸기(maxtix_row 함수 하나로 가로,세로 모두 계산하기 위함)
def matrix_transpose(matrix):
    n = len(matrix)
    result = [[0]*n for _ in range(n)]
 
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix[j][i]
 
    return result
 
 # 흰색 칸 길이가 k보다 큰 경우를 판단하기 위한 함수
def check(matrix, i, j, K):
    if matrix[i][j-1] == 1:
        return False
 
    if matrix[i][j+K] == 1:
        return False
 
    for k in range(K):
        if matrix[i][j+k] == 0:
            return False
 
    return True
 
 # 한 줄 내에서 흰색 칸 길이가 k인 경우 탐지
def check_row(matrix, N, K):
    global answer
    # i = 행 인덱스, j = 열 인덱스
    for i in range(1, N+1):
        for j in range(1, N+2-K):
            if check(matrix, i, j, K):
                answer += 1
 
 
T = int(input())
 
for tc in range(1, T+1):
    N, K = map(int, input().split())
    matrix = [[0]*(N+2)]
 
    for _ in range(N):
        row = [0, *map(int, input().split()), 0]
        matrix.append(row)
 
    matrix.append([0]*(N+2))
 
    answer = 0
    check_row(matrix, N, K)
 
    matrix = matrix_transpose(matrix)
    check_row(matrix, N, K)
 
    print(f'#{tc} {answer}')'''
