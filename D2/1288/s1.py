# 새로운 불면증 치료법

t = int(input())

for tc in range(1, t + 1):
    num_count = [0] * 10
    n = int(input())
    n_origin = n
    while True:
        for sheep_no in str(n):
            num_count[int(sheep_no)] += 1
        if 0 not in num_count:
            break
        n += n_origin

    print(f'#{tc} {n}')
