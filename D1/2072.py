# 홀수만 더하기
T = int(input())
for k in range(1,T+1):
    numbers = list(map(int,input().split()))
    answer = 0
    for i in numbers:
        if i % 2 == 1:
            answer += i
    print('#'+str(k),str(answer),sep=' ')