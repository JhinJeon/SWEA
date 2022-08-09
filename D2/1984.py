# 중간 평균값 구하기

t = int(input())

# 최대값과 최소값을 remove로 제외한 후 평균 구하기(일의 자리까지 반올림)
for tc in range(1, t + 1):
    numbers = list(map(int, input().split()))
    numbers.remove(max(numbers))
    numbers.remove(min(numbers))
    print(f'#{tc} {round(sum(numbers)/len(numbers))}')
