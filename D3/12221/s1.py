# 구구단 2

t = int(input())
for tc in range(1, t + 1):
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        answer = -1
    else:
        answer = a * b
    print(f'#{tc}', answer)
