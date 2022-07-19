# 최대 수 구하기
T = int(input())    #Test case
for k in range(1,T+1):
    num_list = list(map(int,input().split()))   # 숫자를 리스트 형태로 받음
    answer = max(num_list)  # 리스트의 숫자들 중 최대값 반환
    print('#'+str(k),str(answer))