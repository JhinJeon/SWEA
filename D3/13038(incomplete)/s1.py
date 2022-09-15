# 교환학생

t = int(input())

for tc in range(1, t + 1):
    required_day = int(input())
    lecture_week = list(map(int, input().split()))
    answer = 0
    start = False
    while required_day > 0:
        for i in range(7):
            if lecture_week[i] == 1:
                start = True
                required_day -= 1
            elif not start:
                continue
            answer += 1
            if required_day == 0:
                break
    print(f'#{tc}', answer)
