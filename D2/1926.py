# 간단한 369
n = int(input())

# 1부터 n까지의 수가 들어있는 리스트 생성
n_list = [i for i in range(1, n + 1)]

# 리스트의 값들 중 3,6,9가 1개 이상 들어있는 경우 count 적립
for k in n_list:
    count = 0
    if str(k).count('3'):
        count += str(k).count('3')
    if str(k).count('6'):
        count += str(k).count('6')
    if str(k).count('9'):
        count += str(k).count('9')
    if count > 0:
        print(count * '-', end=' ')
    else:
        print(k, end=' ')
