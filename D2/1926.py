# 간단한 369
n = int(input())

n_list = [i for i in range(1, n+1)]

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
