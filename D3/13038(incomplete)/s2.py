# 교환학생
import sys
sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1, t + 1):
    required_day = int(input())
    lecture_week = list(map(int, input().split()))
    answer = 1
    elapsed_date = list()
    date_temp = 0
    for i in range(7):
        if lecture_week[i] == 1:
            elapsed_date.append(date_temp)
            date_temp = 0
        else:
            date_temp += 1

    elapsed_date[0] += date_temp
    elapsed_date.sort(reverse=True)

    while required_day > 0:
        for day in elapsed_date:
            required_day -= 1
            if required_day <= 0:
                break
            answer += day

    print(f'#{tc}', answer)
