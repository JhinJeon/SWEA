# ATM

# 앞 부분을 짧게 만드는 것이 핵심

# n = 사람 수(리스트 길이)
n = int(input())

# waiting = 각자 돈을 인출하는 데 걸리는 시간
waiting = list(map(int, input().split()))

# waiting을 오름차순(작은 값부터) 정렬
waiting.sort(reverse=False)

# 부분 합계 구하기
answer = 0  # answer = 표시할 정답

for i in range(1,n+1):
    answer += sum(waiting[:i])
    
print(answer)