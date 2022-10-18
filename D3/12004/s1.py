# 구구단 1

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    answer = 'No'
    for divider in range(1, 10):
        result = n // divider
        if result < 10 and n % divider == 0:
            answer = 'Yes'
            break

    print(f'#{tc} {answer}')
