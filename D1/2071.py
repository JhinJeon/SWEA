# 평균값 구하기
T = int(input())
for k in range(1,T+1):
    numbers = list(map(int,input().split()))
    answer = int(round(sum(numbers)/len(numbers),0))
    print('#'+str(k),str(answer),sep= ' ')