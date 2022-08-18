# 최빈수 구하기

t = int(input())

for k in range(1, t+1):
    n = int(input())
    scores = list(map(int, input().split()))
    duplicate_count = dict()
    for s in scores:
        temp = 1
        if s not in duplicate_count:
            duplicate_count[s] = temp
        else:
            temp = duplicate_count.get(s)
            duplicate_count[s] = temp + 1
    answer = max(duplicate_count.values())
    duplicated_max = []
    for key, val in duplicate_count.items():
        if val == answer:
            duplicated_max.append(key)

    print(f'#{k} {max(duplicated_max)}')
