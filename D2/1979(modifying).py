#  어디에 단어가 들어갈 수 있을까

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    # 퍼즐 생성
    puzzle = []
    for i in range(n):
        puzzle.append(list(map(int, input().split())))
    answer = 0

    # 가로 퍼즐(정확히 k개의 흰 칸만 있을 때 카운트를 세야 함)
    for col in range(n):
        for row in range(n - k):
            if sum(puzzle[col][row : row + k]) == k:
                if puzzle[col][row + k + 1] == 0:
                    answer += 1

    # 세로 퍼즐
    for i in range(n):
        streakmax = []
        streak = 0
        total = 0
        for j in range(n):  # 세로 인덱스
            if puzzle[j][i] == 1:
                streak += 1
            else:
                streakmax.append(streak)
                streak = 0
        streakmax.append(streak)
        if k in streakmax:
            total = streakmax.count(k)
        answer += total

    print("#" + str(test_case) + " " + str(answer))


'''
구 코드

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int,input().split())
    puzzle = []
    for i in range(n):
        puzzle.append(list(map(int,input().split())))
    answer = 0
    for i in range(n):	#가로 인덱스
        streakmax = []
        streak = 0
        total = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                streak += 1
            else:
                streakmax.append(streak)
                streak = 0
        streakmax.append(streak)
        if k in streakmax:
            total = streakmax.count(k)
        answer += total

    for i in range(n):
        streakmax = []
        streak = 0
        total = 0
        for j in range(n):  # 세로 인덱스
            if puzzle[j][i] == 1:
                streak += 1
            else:
                streakmax.append(streak)
                streak = 0
        streakmax.append(streak)
        if k in streakmax:
            total = streakmax.count(k)
        answer += total

    print("#"+str(test_case)+" "+str(answer))
'''
