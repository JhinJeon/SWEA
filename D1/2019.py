# 더블더블
n = int(input())
answer = 1

for i in range(n+1):
    print(answer * (2 ** i), end =' ')