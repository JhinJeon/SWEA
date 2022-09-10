# 정원

t = int(input())

for tc in range(1,t+1):
    n, d = map(int,input().split())     # d = 분무기 범위, n = 정원 길이
    garden = [i for i in range(1, n+1)]
    answer = 0
    for i in range(d, n, 2*d+1):
        answer += 1
        watered = i
    if watered != n - 1 and watered + d < n - 1:
        answer += 1
    print(f'#{tc} {answer}')


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15]
# d = 3일 때 4에 놓으면 1부터 7까지 커버 가능