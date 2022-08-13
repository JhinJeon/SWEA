# 백만 장자 프로젝트
t = int(input())
for t in range(1, t+1):
    n = int(input())
    market = list(map(int, input().split()))
    profit = 0
    max_price = 0
    for i in range(-1, -n, -1):
        if max_price < market[i]:
            max_price = market[i]
        if market[i-1] < max_price:
            profit += (max_price-market[i-1])
        if market[i-1] > max_price:
            max_price = market[i-1]
    print(f'#{t} {profit}')
