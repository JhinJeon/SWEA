# 24시간

t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())
    time_after = a + b
    if time_after >= 24:
        time_after = time_after % 24
    print(f'#{tc}', time_after)
