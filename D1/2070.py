# 큰 놈, 작은 놈, 같은 놈
T = int(input())
for k in range(1,T+1):
    a, b = map(int,input().split())
    if a < b:
        answer = '<'
    elif a > b:
        answer = '>'
    else:
        answer = '='
    print('#'+str(k),answer)