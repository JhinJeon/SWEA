# 수영장
import sys
sys.stdin = open('sample_input.txt')


def calculation(k, fee):
    global answer
    if k > answer:
        return
    if k > 11:
        if fee < answer:
            answer = fee
        return
    if plan[k]:
        calculation(k+3, fee + quarter)
        calculation(k+1, fee + plan[k])
    else:
        calculation(k+1, fee)


t = int(input())

for tc in range(1, t+1):
    day, month, quarter, year = map(
        int, input().split())    # 이용 요금(일, 월, 3개월, 1년)
    plan = list(map(int, input().split()))       # 이용 계획

    # 일일권과 월별권부터 비교(plan에 저장)
    for i in range(12):
        if plan[i]:
            day_fee = plan[i] * day
            month_fee = month
            plan[i] = min(day_fee, month_fee)

    answer = max(day, month, quarter, year) * 12
    # 월별권과 3개월권 비교
    calculation(0, 0)

    # 1년권이 더 싼지 비교
    if answer > year:
        answer = year

    print(f'#{tc}', answer)
