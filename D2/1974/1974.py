# 스도쿠 검증

# 개선한 코드

t = int(input())
sudoku = []

# 스도쿠 값 추가
# input이 한번에 9개의 스도쿠 판을 받는 형태
for i in range(t*9):
    sudoku.append(list(map(int, input().split())))

# input으로 받은 길쭉한 스도쿠 판을 9 * 9 사이즈의 부분만 보기
# input을 9배수 단위로 나누어서 graph에 임시 저장

# 스도쿠 검증은 1부터 9까지의 숫자가 빠짐없이 있는지 확인하는 방식으로 구현
# temp = 숫자 중복 여부를 판단하는 임시 리스트
for x in range(t):
    answer = 1
    graph = sudoku[x*9:(x+1)*9]
    # 가로 검증
    for i in range(9):
        temp = [0] * 10
        for j in range(9):
            temp[graph[i][j]] += 1
        if temp.count(1) != 9:
            answer = 0
    if answer == 0:
        print(f'#{x + 1} 0')
        continue
    # 세로 검증
    for i in range(9):
        temp = [0] * 10
        for j in range(9):
            temp[graph[j][i]] += 1
        if temp.count(1) != 9:
            answer = 0
    if answer == 0:
        print(f'#{x + 1} 0')
        continue

    # 구역(3 * 3) 검증

    for a in range(0, 7, 3):
        for b in range(0, 7, 3):
            temp = [0] * 10
            for c in range(3):
                for d in range(3):
                    temp[graph[a+c][b+d]] += 1
            if temp.count(1) != 9:
                answer = 0
                continue

    print(f'#{x+1} {answer}')

'''
구 코드(1)
import sys
sys.stdin = open("input.txt")

t = int(input())
sudoku = []

# 스도쿠 값 추가
# input이 한번에 9개의 스도쿠 판을 받는 형태
for i in range(t*9):
    sudoku.append(list(map(int, input().split())))

# input으로 받은 길쭉한 스도쿠 판을 9 * 9 사이즈의 부분만 보기
# input을 9배수 단위로 나누어서 graph에 임시 저장

# 스도쿠 검증은 1부터 9까지의 숫자가 빠짐없이 있는지 확인하는 방식으로 구현
# temp = 숫자 중복 여부를 판단하는 임시 리스트
for x in range(t):
    answer = 1
    graph = sudoku[x*9:(x+1)*9]
    # 가로 검증
    for i in range(9):
        temp = [0] * 10
        for j in range(9):
            temp[graph[i][j]] += 1
        if temp.count(1) != 9:
            answer = 0
    if answer == 0:
        print(f'#{x + 1} 0')
        continue
    # 세로 검증
    for i in range(9):
        temp = [0] * 10
        for j in range(9):
            temp[graph[j][i]] += 1
        if temp.count(1) != 9:
            answer = 0
    if answer == 0:
        print(f'#{x + 1} 0')
        continue

    # 구역(3 * 3) 검증

    for a in range(0, 7, 3):
        for b in range(0, 7, 3):
            temp = [0] * 10
            for c in range(3):
                for d in range(3):
                    temp[graph[a+c][b+d]] += 1
            if temp.count(1) != 9:
                answer = 0
                continue

    print(f'#{x+1} {answer}')
'''

'''
구 코드(2)
t = int(input())
sudoku = []
for i in range(t*9):
    sudoku.append(list(map(int,input().split())))
for x in range(t):
    temp = []    
    answer = 1
    graph = sudoku[x*9:(x+1)*9]
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(graph[i][j])
        bucket = list(set(temp))
        if len(bucket) != 9:
            answer = 0
            continue
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(graph[j][i])
        bucket = list(set(temp))
        if len(bucket) != 9:
            answer = 0
            continue
    temp = []
    for a in range(0,7,3):
        for b in range(0,7,3):
            for c in range(3):
                for d in range(3):
                    temp.append(graph[a+c][b+d])
            bucket = list(set(temp))
            if len(bucket) != 9:
                answer = 0
                continue
            else:
                temp = []
    print('#'+str(x+1)+' '+str(answer))
'''
