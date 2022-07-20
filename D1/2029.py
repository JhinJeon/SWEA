# 몫과 나머지 출력하기
t = int(input())
for k in range(1,t+1):
    a, b = map(int,input().split())
    print('#'+str(k),str(a//b),str(a%b))