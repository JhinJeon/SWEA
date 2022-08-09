# 지그재그 숫자

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    answer = 0
    # 1 부터 n까지의 범위
    # 짝수는 빼고 홀수는 더하기
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer -= i
        else:
            answer += i
    print(f'#{tc} {answer}')
