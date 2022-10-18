# 평범한 숫자

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    array = list(map(int, input().split()))
    min_value = min(array)
    max_value = max(array)

    answer = 0
    for idx in range(1, n-1):
        if min_value < array[idx] < max_value:
            if array[idx-1] <= array[idx] <= array[idx+1]:
                answer += 1
            elif array[idx-1] >= array[idx] >= array[idx+1]:
                answer += 1

    print(f'#{tc}', answer)
