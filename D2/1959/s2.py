# 숫자를 정렬하자

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    # list_n, list_m = 입력받는 숫자열을 리스트로 변환해서 저장
    # answer = 숫자들의 곱을 합한 값들 중 최댓값
    list_n = list(map(int, input().split()))
    list_m = list(map(int, input().split()))
    answer = 0

    # list_n이 list_m보다 길이가 긴 경우
    if n > m:
        for i in range(n-m+1):
            # answer_temp = 숫자들의 곱의 합계를 임시로 저장하는 변수
            answer_temp = 0

            # list_m은 처음부터, list_n은 i로 보정된 값만큼 인덱스를 조정
            # 곱한 값을 임시 변수에 저장
            for idx in range(m):
                answer_temp += list_n[idx+i] * list_m[idx]

            # answer_temp이 최댓값인 경우 answer 갱신
            if answer_temp >= answer:
                answer = answer_temp

    # 그 외의 경우(리스트 길이가 같은 경우 포함)
    # 리스트 길이가 동등한 경우 i는 0만 반환됨
    else:
        for i in range(m-n+1):
            # answer_temp = 숫자들의 곱의 합계를 임시로 저장하는 변수
            answer_temp = 0

            # list_n은 처음부터, list_m은 i로 보정된 값만큼 인덱스를 조정
            # 곱한 값을 임시 변수에 저장
            for idx in range(n):
                answer_temp += list_n[idx] * list_m[idx+i]

            # answer_temp이 최댓값인 경우 answer 갱신
            if answer_temp >= answer:
                answer = answer_temp

    print(f'#{tc} {answer}')
