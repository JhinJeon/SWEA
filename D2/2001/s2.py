# 파리 퇴치
t = int(input())
for k in range(t):
    n, m = map(int, input().split())
    area = []
    score = []
    for i in range(n):
        area.append(list(map(int, input().split())))
    for column in range(n - m + 1):
        for row in range(n - m + 1):
            kill = 0
            for y in range(m):
                for x in range(m):
                    kill += area[column + y][row + x]
            score.append(kill)

    print(f"#{k+1} {max(score)}")
