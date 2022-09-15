# 교환학생
# 테스트 케이스에서 1개가 틀리는 문제 발생

# import sys

# sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1, t + 1):
    required_day = int(input())  # 수업을 들어야 하는 날짜 수
    lecture_week = list(map(int, input().split()))
    answer = 1                  # 총 출석일(출력값)
    elapsed_date = list()       # 다음 수업까지의 기간 리스트
    date_temp = 0               # 다음 수업까지의 기간 계산용 임시 변수
    for i in range(7):
        # 수업일인 경우 elapsed_time에 추가
        if lecture_week[i] == 1:
            elapsed_date.append(date_temp)
            date_temp = 0
        date_temp += 1

    elapsed_date[0] += date_temp            # 주 바뀜  공백 계산

    # 수업 일수를 최소화하도록 오름차순 정렬 <- 요 부분에서 문제가 있지 않을까 싶다.
    elapsed_date.sort(reverse=False)

    # 수업을 들어야 하는 날이 이틀 이상 남은 경우(1일인 경우 answer=1이므로 1로 반환됨)
    while required_day > 1:
        for day in elapsed_date:    # 들어야 하는 날짜 수를 1 차감하고 다음 수업까지의 기간 계산
            required_day -= 1
            answer += day

            # 필요한 시수를 다 채운 경우 반복문 종료
            if required_day <= 1:
                break

    print(f'#{tc}', answer)

# 1 1 0 1 1 0 0
# 이 경우 1일 - 4일 - 2일 (2일 - 1일 - 4일) 주기로 반복인데 내림차순으로 정렬해서 1 - 2 - 4로 만들어버리는 문제가 있다.
