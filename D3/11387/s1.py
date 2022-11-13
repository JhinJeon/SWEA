# 몬스터 사냥

t = int(input())

for tc in range(1, t+1):
    d, l, n = map(int, input().split())
    total = 0   # 총 가한 피해
    ratio = l * 0.01    # 피해량 증폭 계수

    for turn in range(n):
        total += d * (1 + turn * ratio)

    print(f'#{tc}', int(total))
