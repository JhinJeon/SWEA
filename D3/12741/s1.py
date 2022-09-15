# 두 전구

t = int(input())
result = list()
for tc in range(1, t+1):
    a_on, a_off, b_on, b_off = map(int, input().split())
    overlap_start = a_on if a_on > b_on else b_on
    overlap_end = a_off if a_off < b_off else b_off
    answer = len(range(overlap_start, overlap_end))
    result.append(answer)

# 테스트 케이스가 많은 문제(수만 개 이상)인 경우 결과를 리스트에 모아 놓고 출력하는 게 시간절약에 유리함
for idx, val in enumerate(result):
    print(f'#{idx+1}', val)
