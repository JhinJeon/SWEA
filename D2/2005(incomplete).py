# 파스칼의 삼각형
t = int(input())

for k in range(1, t+1):
    n = int(input())
    for i in range(n):
        if i == 0 or i == 1:
            print('1' * (i+1))
        else:
            print('1'+str(i) * 2 + '1')
