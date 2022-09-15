# 교환학생

# import sys
#
# sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1, t + 1):
    required_day = int(input())  # 수업을 들어야 하는 날짜 수
    lecture_week = list(map(int, input().split()))
    elapsed_date = list()       # 다음 수업까지의 기간 리스트
    date_temp = 0               # 다음 수업까지의 기간 계산용 임시 변수
    for i in range(7):
        # 수업일인 경우 elapsed_time에 추가
        if lecture_week[i] == 1:
            elapsed_date.append(date_temp)
            date_temp = 0
        date_temp += 1

    elapsed_date[0] += date_temp            # 주 바뀜  공백 계산

    answer_case = list()
    cases = len(elapsed_date)
    for case in range(cases):
        result = 1
        countdown = 1
        # 수업을 들어야 하는 날이 이틀 이상 남은 경우(1일인 경우 answer=1이므로 1로 반환됨)
        while countdown < required_day:
            for idx in range(cases):    # 들어야 하는 날짜 수를 1 차감하고 다음 수업까지의 기간 계산
                countdown += 1
                result += elapsed_date[(case+idx) % cases]

                # 필요한 시수를 다 채운 경우 반복문 종료
                if countdown == required_day:
                    break
        answer_case.append(result)

    print(f'#{tc}', min(answer_case))
