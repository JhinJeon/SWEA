# 벌꿀 채취
# the_gathering의 계산 알고리즘 문제 - 합계 제한을 넘지 않도록 하는 벌꿀 조합을 구성해서 수익을 구해야 함

import sys
sys.stdin = open('sample_input.txt')


# 벌꿀 채취 블록 선택 조합 경우의 수 도출
def combinations_gathering(arr, k, idx):
    global collect_cases, part_array
    if sum(arr) > gather_limit:
        return
    if len(arr) == k:
        collect_cases.append(list(arr))
    for c in range(idx, m):
        arr.append(part_array[c])
        combinations_gathering(arr, k, c+1)
        arr.pop()


# 벌꿀 채취 조합 경우의 수 도출
def combinations(arr, idx):
    global case_combinations
    if len(arr) == 2:
        case_combinations.append(list(arr))
        return
    for c in range(idx, len(cases)):
        arr.append(cases[c])
        combinations(arr, c+1)
        arr.pop()


t = int(input())

for tc in range(1,t+1):
    # n = 그래프 너비, m = 선택하는 칸 개수, gather_limit = 선택한 칸의 값들의 합계 제한
    n, m, gather_limit = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(n)]
    small = True if (n // 2) >= m else False
    cases = []  # 채취 경우의 수 저장
    case_combinations = []  # 조합 경우의 수 저장

    # 채취 경우의 수 생성
    for col in range(n):
        for row in range(n - m + 1):
            part_array = graph[col][row:row + m]
            # 벌꿀 한도를 넘지 않는 경우의 수 도출
            collect_cases = []  # 구역 내 채집 경우의 수
            max_revenue = 0     # 구역 내 최대 수익
            for i in range(1, m+1):
                combinations_gathering([], i, 0)

            for cc in collect_cases:
                temp_value = 0
                for honey in cc:
                    temp_value += honey ** 2
                if temp_value > max_revenue:
                    max_revenue = temp_value
            cases.append((max_revenue, row, col))

    # 채취 경우의 수를 2개씩 묶어서 조합 생성
    combinations([], 0)

    # 각 조합이 유효한지 확인
    answer = 0
    for case_a, case_b in case_combinations:
        # 채취 영역이 겹치는 경우
        if case_a[2] == case_b[2] and case_a[1] + m > case_b[1]:
            continue
        # 그 외의 경우에는 채취 결과 합산
        value = case_a[0] + case_b[0]
        
        # 최댓값 경신인 경우
        if value > answer:
            answer = value
            
    print(f'#{tc}', answer)