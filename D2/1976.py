# 시각 덧셈

t = int(input())

for tc in range(1, t+1):
    # 입력받는 값 : 시 1, 분 1, 시 2, 분 2
    time_1, minute_1, time_2, minute_2 = map(int, input().split())
    # 시 합계와 분 합계 계산
    time_sum = time_1 + time_2
    minute_sum = minute_1 + minute_2

    # 분 합계가 60을 초과하는 경우 시 합계 +1
    if minute_sum >= 60:
        minute_sum -= 60
        time_sum += 1
    # 시 단위를 12시간제로 정리
    if time_sum >= 13:
        time_sum -= 12
    print(f'#{tc} {time_sum} {minute_sum}')
